import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class AuthService {
  private apiUrl = 'http://localhost:8000';

  constructor(private http: HttpClient) {}

  login(email: string, password: string) {
    const body = new URLSearchParams();
    body.set('username', email);
    body.set('password', password);
  
    return this.http.post<{ access_token: string }>(
      `${this.apiUrl}/auth/login`,
      body.toString(),
      {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        }
      }
    );
  }

  saveToken(token: string) {
    localStorage.setItem('access_token', token);
  }

  getToken(): string | null {
    return localStorage.getItem('access_token');
  }

  isAuthenticated(): boolean {
    return !!this.getToken();
  }

  logout() {
    localStorage.removeItem('access_token');
  }
}
