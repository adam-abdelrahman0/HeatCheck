import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss',
})
export class AppComponent {
  title = 'angular-frontend';
  leaderboard: any[] = [];

  constructor(private http: HttpClient) {}

  ngOnInit() {
    this.getLeaderboard();
  }

  getLeaderboard() {
    this.http.get('http://127.0.0.1:5000/leaderboard').subscribe((data: any) => {
      this.leaderboard = data;
      console.log('Leaderboard:', this.leaderboard);
    });
  }

  submitScore(outfitData: any) {
    this.http.post('http://127.0.0.1:5000/submit-score', outfitData).subscribe(response => {
      console.log('Score submitted:', response);
    });
  }
}
