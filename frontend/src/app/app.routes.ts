import { Routes } from '@angular/router';
import { LoginComponent } from './auth/login/login.component';
import { AuthGuard } from './auth/auth.guard';

export const routes: Routes = [
  { path: 'login', component: LoginComponent },

  {
    path: 'trips',
    canActivate: [AuthGuard],
    loadComponent: () =>
      import('./trips/trips.component')
        .then(m => m.TripsComponent)
  },

  { path: '', redirectTo: 'login', pathMatch: 'full' },
  { path: '**', redirectTo: 'login' }
];
