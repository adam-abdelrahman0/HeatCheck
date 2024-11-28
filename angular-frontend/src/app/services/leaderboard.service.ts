import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { LeaderboardEntry } from '../types/leaderboard-entry';

@Injectable({
    providedIn: 'root',
})
export class LeaderboardService {
    private leaderboardUrl = 'http://localhost:5000/api/leaderboard';
    private leaderboard: LeaderboardEntry[] = [];

    constructor(private http: HttpClient) {}

    fetchLeaderboard(): Observable<LeaderboardEntry[]> {
        return this.http.get<LeaderboardEntry[]>(this.leaderboardUrl);
    }

    getLeaderboard(): LeaderboardEntry[] {
        return this.leaderboard;
    }

    setLeaderboard(data: LeaderboardEntry[]): void {
        this.leaderboard = data;
        this.leaderboard.sort((a, b) => b.score - a.score);
    }
}