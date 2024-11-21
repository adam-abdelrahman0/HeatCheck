import { Component, ElementRef, ViewChild } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-webcam',
  templateUrl: './webcam.component.html',
  styleUrls: ['./webcam.component.scss']
})
export class WebcamComponent {
  @ViewChild('webcam') webcam!: ElementRef<HTMLVideoElement>;
  @ViewChild('snapshotCanvas') snapshotCanvas!: ElementRef<HTMLCanvasElement>;

  capturedImage: string | null = null;

  constructor(private http: HttpClient) {}

  ngAfterViewInit() {
    this.startWebcam();
  }

  startWebcam() {
    navigator.mediaDevices.getUserMedia({ video: true })
      .then((stream) => {
        const videoElement = this.webcam.nativeElement;
        videoElement.srcObject = stream;
        videoElement.play();
    })
      .catch((error) => {
        console.error('Error accessing webcam:', error);
      });
  }

  captureImage() {
    const videoElement = this.webcam.nativeElement;
    const canvasElement = this.snapshotCanvas.nativeElement;
    const ctx = canvasElement.getContext('2d');

    canvasElement.width = videoElement.videoWidth;
    canvasElement.height = videoElement.videoHeight;

    if (ctx) {
      ctx.drawImage(videoElement, 0, 0, canvasElement.width, canvasElement.height);
      this.capturedImage = canvasElement.toDataURL('image/jpeg');
      this.sendImageToBackend(this.capturedImage);
    }
  }

  sendImageToBackend(imageData: string) {
    // Remove the "data:image/jpeg;base64," prefix
    const base64Image = imageData.split(',')[1];
    this.http.post('/process-image', { image: base64Image })
      .subscribe((response: any) => {
        console.log('Backend response:', response);
        alert(`Score: ${response.score}`);
    }, (error) => {
        console.error('Error processing image:', error);
        alert('Failed to process the image.');
      });
  }
}

