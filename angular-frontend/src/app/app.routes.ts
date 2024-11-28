import { RouterModule, Routes } from '@angular/router';
import { WebcamComponent } from './components/webcam/webcam/webcam.component';
import { HomeComponent } from './components/home/home-component/home-component.component';
import { NgModule } from '@angular/core';


export const routes: Routes = [
    { path: '', redirectTo: '/home', pathMatch: 'full' }, // Redirect to home by default
    { path: 'home', component: HomeComponent }, // Replace with your HomeComponent
    { path: 'webcam', component: WebcamComponent }, // Route to WebcamComponent
    ];
@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
})
export class AppRoutingModule { }