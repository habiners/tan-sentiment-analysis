import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  title = 'tan-sentiment-analysis';

  userInput: string;
  cleaned: string;
  sentiment: JSON; // Server Data

  constructor(private httpClient: HttpClient) {}
  ngOnInit() {}

  // #Coachella2015 tickets selling out in less than 40 minutes _Ù_¦_Ù___Ù___Ù÷_ÙÎµ_ÙÎµ_Ù___Ù_¦ http://t.co/SmoXyteIMJ
  async getSentiment() {
    // this.sentiment = null;
    this.cleaned = this.userInput.replace(/([^\w\s]|_|[^\x00-\x7F])+/g, "");
    this.sentiment = await this.httpClient.get('http://127.0.0.1:5002/sentiment-analysis/' + this.cleaned).toPromise() as JSON;
  }
}
