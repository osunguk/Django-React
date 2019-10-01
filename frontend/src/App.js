import React, { Component } from 'react';
import { Link, Route, BrowserRouter as Router } from "react-router-dom";
import test from './test'
import auth from './auth'


class App extends Component {
  state = {
    posts: [],
    users: []
  };

  componentDidMount() {
    fetch('http://127.0.0.1:8000/api/users/')
      .then(res => res.json())
      .then(json => {
        console.log(json)
        this.setState({
          users: json
        })
      })
    fetch('http://127.0.0.1:8000/api/')
      .then(res => res.json())
      .then(
        json => this.setState({
          posts: json
        })
      )
  }

  handle_KakaoLogout(){
    var host = 'http://127.0.0.1:8000/logout/'


  }

  handle_KakaoLogin() {
    var host = 'https://kauth.kakao.com'
    var client_id = '2164b8cf12e0e79b610070b46396fc28'
    // var redirect_uri = 'http://localhost:3000'
    var redirect_uri = 'http://127.0.0.1:8000/auth/'
    var url = `${host}/oauth/authorize?client_id=${client_id}&redirect_uri=${redirect_uri}&response_type=code`
    console.log('url :', url)
    fetch(url)
      .then(
        res => {
          console.log('res', res)
          window.open(res.url, '카카오 로그인', 'width=570, height=490, top=250, left=500')
        })
    // .then(
    //   json => console.log('json',json)
    // )
  }

  render() {
    return (
      <div>
        <Router>
        <header>
          <Link to='/test'>
            <button>test</button>
          </Link>
          
        </header>
        <hr />
        <main>
          <switch>
            <Route path='/test' component={test} />
            <Route path='/auth' component={auth} />
          </switch>
        </main>
      </Router>
        <div id='카카오 로그인'>
          <h3>카카오 로그인</h3>
          <button onClick={this.handle_KakaoLogin}>로그인</button>
          <button onClick={this.handle_KakaoLogout}>로그아웃</button>
        </div>
        {this.state.users.map(item => (
          <div key={item.id}>
            <h1>{item.username}님 반갑습니다!</h1>
            <p>{item.email}</p>
          </div>
        ))}
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