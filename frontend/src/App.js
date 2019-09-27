import React, { Component } from 'react';


const style = {
  image: {
    border: '1px solid #ccc',
    background: '#fefefe',
  },
};

class App extends Component {
  state = {
    posts: [],
    users: []
  };

  componentDidMount() {
    console.log('a')
    fetch('http://127.0.0.1:8000/api/users/')
      .then(res => res.json())
      .then(json => {
        console.log(json)
        this.setState({
          users: json
        })
      })

    console.log('b')
    fetch('http://127.0.0.1:8000/api/')
      .then(res => res.json())
      .then(
        json => this.setState({
          posts: json
        })
      )
    console.log('c')
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
        {this.state.users.map(item => (
          <div key={item.id}>
            <h1>{item.username}</h1>
            <p>{item.email}</p>
            <img
              src={item.image}
              alt='No img'
              height={240}
              width={240}
              style={style.image
              }
            />
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