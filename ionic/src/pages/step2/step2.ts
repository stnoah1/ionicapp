import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { Api } from '../../providers';
import { MainPage } from '../';


/**
 * Generated class for the Step2Page page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-step2',
  templateUrl: 'step2.html',
})
export class Step2Page {
  user_info: { first_name : string, phone: string, gender: string, birthday: string, current_join_step: string};
  token :string;

  constructor(public navCtrl: NavController, public navParams: NavParams, public api: Api) {
    this.user_info = this.navParams.get('user_info');
    this.token = this.navParams.get('token');
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad Step2Page');
  }
  goBack(data){
    this.patch(data);
    this.navCtrl.push('Step1Page');
  }
  goNext(data){
    this.patch(data);
    this.navCtrl.push('Step3Page');
  }
  patch(modData){
    var headers = new HttpHeaders().set('Authorization', 'Token ' + this.token);
    var _body = {"gender": modData};
    let usrInfo = this.api.patch('users/self/', _bodY, { headers: headers}).share();
    usrInfo.subscribe((usrRes: any) => {
      if(usrRes){
        this.user_info = usrRes;
        console.log(usrRes);
      }else{
        console.log('사용자 정보를 조회할 수 없음.');
      }
    }, err => {
      console.error('ERROR', err);
    });

  }
}
