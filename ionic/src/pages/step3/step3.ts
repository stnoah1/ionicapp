import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { MainPage } from '../';


/**
 * Generated class for the Step3Page page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-step3',
  templateUrl: 'step3.html',
})
export class Step3Page {

  constructor(public navCtrl: NavController, public navParams: NavParams) {
  }
  goBack(){
    // 저장 patch
    this.navCtrl.push('Step2Page');
  }
  goMain(){
    // 저장 patch
    this.navCtrl.push(MainPage);
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad Step3Page');
  }

}
