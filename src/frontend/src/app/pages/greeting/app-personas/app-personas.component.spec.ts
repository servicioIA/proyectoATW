import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AppPersonasComponent } from './app-personas.component';

describe('AppPersonasComponent', () => {
  let component: AppPersonasComponent;
  let fixture: ComponentFixture<AppPersonasComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AppPersonasComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(AppPersonasComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
