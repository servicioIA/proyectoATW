import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AppGreetingComponent } from './app-greeting.component';

describe('AppGreetingComponent', () => {
  let component: AppGreetingComponent;
  let fixture: ComponentFixture<AppGreetingComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AppGreetingComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(AppGreetingComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
