import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MaterialModule } from '../../material.module';

// icons
import { TablerIconsModule } from 'angular-tabler-icons';
import * as TablerIcons from 'angular-tabler-icons/icons';

import { GreetingRoutes } from './greeting.routing';
import { AppGreetingComponent } from './app-greeting/app-greeting.component';
import { AppPersonasComponent } from './app-personas/app-personas.component';
import { SweetAlert2Module } from '@sweetalert2/ngx-sweetalert2';

@NgModule({
  imports: [
    CommonModule,
    RouterModule.forChild(GreetingRoutes),
    MaterialModule,
    FormsModule,
    ReactiveFormsModule,
    TablerIconsModule.pick(TablerIcons),
    SweetAlert2Module,
  ],
  declarations: [
    AppGreetingComponent,
    AppPersonasComponent
  ],
})
export class GreetingModule {}
