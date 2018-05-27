import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { Api } from '../../providers';
/**
 * Generated class for the Step1Page page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-step1',
  templateUrl: 'step1.html',
})
export class Step1Page {
  user_info: { first_name : string, phone: string, gender: string, birthday: string, current_join_step: string};
  constructor(public navCtrl: NavController, public navParams: NavParams, public api: Api) {
    this.user_info = this.navParams.get('user_info');
    console.log(this.user_info.first_name);
  }
  goNext(){
    // 저장 patch
    console.log(this.user_info);
    this.navCtrl.push('Step2Page');
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad Step1Page');
  }

}
