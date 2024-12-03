import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import { LeaderboardService } from '../../../services/leaderboard.service';
import { LeaderboardEntry } from '../../../types/leaderboard-entry';
import { FormsModule } from "@angular/forms"
import { Score } from '../../../types/score';

@Component({
  selector: 'app-home-component',
  imports: [CommonModule, FormsModule],
  templateUrl: './home-component.component.html',
  styleUrl: './home-component.component.scss'
})
export class HomeComponent {
  uploadedImage: string | null = null;
  leaderboard: LeaderboardEntry[] = [];
  outfitScore: number | null = null;
  isModalVisible = false;
  isLoading = false;
  username: string = "newsample";
  constructor(private http: HttpClient, private leaderboardService: LeaderboardService) {}

  ngOnInit() {
    this.leaderboard = this.leaderboardService.getLeaderboard();
    console.log(this.leaderboard)
  }

  // Handle drag over event
  onDragOver(event: DragEvent): void {
      event.preventDefault();
      const dropArea = event.target as HTMLElement;
      dropArea.classList.add('active');
  }

  // Handle drag leave event
  onDragLeave(event: DragEvent): void {
      const dropArea = event.target as HTMLElement;
      dropArea.classList.remove('active');
  }

  // Handle drop event
  onDrop(event: DragEvent): void {
      event.preventDefault();
      const dropArea = event.target as HTMLElement;
      dropArea.classList.remove('active');

      const files = event.dataTransfer?.files;
      if (files && files.length > 0) {
          this.handleFileUpload(files[0]);
      }
  }

  // Handle file selection through input
  onFileSelected(event: Event): void {
      const input = event.target as HTMLInputElement;
      if (input.files && input.files.length > 0) {
          this.handleFileUpload(input.files[0]);
      }
  }

  // Process file and convert to Base64
  handleFileUpload(file: File): void {
      if (file.type !== 'image/jpeg') {
          alert('Only JPG files are allowed!');
          return;
      }

      const reader = new FileReader();
      reader.onload = () => {
          this.uploadedImage = reader.result as string;
          //this.sendImageToBackend(this.uploadedImage);
      };
      reader.readAsDataURL(file);
  }

  // Send Base64 image to the backend
  sendImageToBackend(base64Image: string): void {
    this.isLoading = true;
    this.isModalVisible = true;

    if (!this.uploadedImage) {
      alert('No image to send!');
      this.closeModal();
      this.isLoading = false;
      return;
    }

    this.http.post<{ message: string; ranking_score: number; result: any }>('http://127.0.0.1:5000/process-image', { image: this.uploadedImage, username: this.username })
      .subscribe({
          next: (response) => {
            this.outfitScore = response.ranking_score;
            this.updateLeaderboard(this.username, this.outfitScore as number);
            console.log(this.outfitScore);
            console.log('Image sent successfully:', response);
            this.isLoading = false;
          },
          error: (error) => {
            console.error('Error sending image:', error);
            this.isLoading = false;
            alert('Failed to process image.');
          },
      });

      this.leaderboard = this.leaderboardService.getLeaderboard();
    }

    closeModal() {
        this.isModalVisible = false;
        this.outfitScore = null;
    }

    // only for client side: the actual leaderboard is also updated in the backend
    updateLeaderboard(username: string, score: number) {
        this.leaderboard.push({ username, score });
        this.leaderboard.sort((a, b) => b.score - a.score); // Keep leaderboard sorted by score
      }
}
