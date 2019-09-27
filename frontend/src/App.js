import React, { Component } from 'react';

class App extends Component {
  state = {
    posts: []
  };

  componentDidMount() {

    fetch('http://127.0.0.1:8000/api/')
      .then(res => res.json())
      .then(
        json => this.setState({
          posts: json
        })
      )
  }

  handle_KakaoLogin(){
    var host = 'https://kauth.kakao.com'
    var client_id = '2164b8cf12e0e79b610070b46396fc28'
    // var redirect_uri = 'http://localhost:3000'
    var redirect_uri = 'http://127.0.0.1:8000/auth/'
    var url = `${host}/oauth/authorize?client_id=${client_id}&redirect_uri=${redirect_uri}&response_type=code`
    console.log('url :',url)
    fetch(url)
    .then(
      res => {
        console.log('res',res)
        window.open(res.url)
      })
    // .then(
    //   json => console.log('json',json)
    // )
  }

  render() {
    return (
      <div>
        <div id='카카오 로그인'>
          <h3>카카오 로그인</h3>
          <button onClick={this.handle_KakaoLogin}>로그인</button>
        </div>
        {this.state.posts.map(item => (
          <div key={item.id}>
            <h1>{item.title}</h1>
            <span>{item.content}</span>
          </div>
        ))}
      </div>
    );
  }
}

export default App;