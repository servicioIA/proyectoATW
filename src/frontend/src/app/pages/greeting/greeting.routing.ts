import { Routes } from '@angular/router';


// pages
import { AppGreetingComponent } from './app-greeting/app-greeting.component';
import { AppPersonasComponent } from './app-personas/app-personas.component';

export const GreetingRoutes: Routes = [
  {
    path: '',
    component: AppGreetingComponent,
  },
  {
    path: 'people',
    component: AppPersonasComponent,
  },
];
