import { Component } from '@angular/core';
import { TranslateService } from '@ngx-translate/core';
import { IonicPage, NavController, ToastController } from 'ionic-angular';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { User, Api } from '../../providers';
import { MainPage } from '../';
import { SignupPage } from '../signup/signup';


@IonicPage()
@Component({
  selector: 'page-login',
  templateUrl: 'login.html'
})
export class LoginPage {
  // The account fields for the login form.
  // If you're using the username field with or without email, make
  // sure to add it to the type
  account: { uuid: string, token: string} = {
    token: 'b676fd54152822db186944c24399c2ac93c2cc7e',
    uuid: '12341234'
  };
  user_info: { first_name : string, phone: string, gender: string, birthday: string, current_join_step: string}; 


  // Our translated text strings
  private loginErrorString: string;

  constructor(public navCtrl: NavController, public user: User, public api: Api){}

  // Attempt to login in through our User service
  doLogin() {
    this.user.login(this.account).subscribe((resp) => {
      if (resp){
        var headers = new HttpHeaders().set('Authorization', 'Token ' + resp['token'])
        let usrInfo = this.api.get('users/self', '', { headers: headers}).share();
        usrInfo.subscribe((usrRes: any) => {
          let user_params = {'user_info':this.user_info, 'token':resp['token']};
          if(usrRes){
            this.user_info = usrRes;
            switch (usrRes['current_join_step']){
              case 'name':
                this.navCtrl.push('Step1Page', user_params);
                break;
              case 'gender':
                this.navCtrl.push('Step2Page', user_params);
                break;
              case 'age':
                this.navCtrl.push('Step3Page', user_params);
                break;
              default:
                this.navCtrl.push(MainPage, user_params);
              }
          }else{
            console.log('사용자 정보를 조회할 수 없음.');
          }
        }, err => {
          console.error('ERROR', err);
        });
      }else{
        this.navCtrl.push('SignupPage');
      }
    }, (err) => {
      console.log('Error', err);
      // Unable to log in
    });
  }
}
