import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { Http, Headers, RequestOptions } from '@angular/http';
import { Api } from '../../providers/api/api';
import { HttpClient, HttpHeaders } from '@angular/common/http';

/**
 * Generated class for the UuidtestPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-uuidtest',
  templateUrl: 'uuidtest.html',
})
export class UuidtestPage {
  data:any = {};
  deviceInfo = {}
  token;
 
  constructor(public navCtrl: NavController, public http: Http, public api: Api) {}

  onLogin() {
    var _body = {device_unique_key: this.deviceInfo['uuid']};
    var headers = new HttpHeaders().set('Authorization', 'Token b676fd54152822db186944c24399c2ac93c2cc7e')
    // headers.set('Content-Type', 'application/json')
    this.api.post('token', _body, {headers: headers})
    .subscribe(data => {
      if (data){
        this.navCtrl.push('TabsPage', {'userToken':data});
      }else{
        this.navCtrl.push('SignupPage');
      }
    }, error => {
      console.error('ERROR', error);
    });
  }
}
