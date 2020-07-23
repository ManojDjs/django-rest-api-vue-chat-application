<template>
  <div class="container">
  <div class="row">
            <!-- <h3>{{ currentuser.username }}</h3> -->
            <div class="col col-lg-4 float-right scrolluser">
             <button type="button" class="btn btn-primary btn-block outline">Users online</button>
              <ul class="list-group">

                <a
                  class="list-group-item list-group-item-action"
                  @click="get_chat(user.username)"
                  v-for="(user,index) in users"
                  v-bind:key="index" 
                >
                <div v-if="user.username!==currentuser.username"><img src="../assets/user.png" class="img-circle"  alt="image" >
                <h1 style="font: italic small-caps bold 20px/30px Georgia, serif;">{{ user.username }}</h1></div></a>
              </ul>
            </div>
        <div class="col float-left">
          <div class="overflow-auto" id='mid'>
          <div class="panel panel-primary">
            <div class="panel-heading" id="accordion" v-if="selected">
              <span class="glyphicon glyphicon-comment"></span>
              <button type="button" class="btn btn-primary btn-block outline">CHAT</button>
              <h4>{{ selected }}</h4>
                  <ul class="list-group" style=" height: 500px; overflow: auto">
                    <!-- {{ currentuser.username }} -->
                    <!-- {{ selected }} -->
                    <li  class="list-group-item" v-for="(message,index) in messages" v-bind:key="index">

                    <blockquote class="blockquote text-right" v-if="message.sender===currentuser.username || message.sender===currentuser.username">
                    <p class="mb">{{ message.text }}</p>

                    <footer class="blockquote-footer">You<cite title="Source Title">{{ message.time }}</cite></footer>
                  </blockquote>
                  <blockquote class="blockquote text-left" v-else>
                    <p class="mb">{{ message.text }}</p>

                    <footer class="blockquote-footer" >{{ selected }}<cite title="Source Title">{{ message.time }}</cite></footer>
                  </blockquote>
                    </li>
                  </ul>
              <emoji-picker
                  :selected="selected"
                  :currentuser="currentuser.username"
                  v-on:get_chat="get_chat(selected)"
                  @selectedemoji="text=$event"
                ></emoji-picker>
            </div>
          </div>
          </div>
        </div>
  </div>
  </div>
      


    <!-- <HelloWorld msg="Welcome to Your Vue.js App" /> -->
  
</template>

<script>

// import { apiService } from "@/common/api.service.js";
import axios from 'axios';
import emoji from "@/components/emoji.vue";
import { CSRF_TOKEN } from "@/common/csrftoken.js"
export default {
  data(){
    return{
    users:[],
    info:null,
    selected:'',
    messages:[],
    currentuser:''
    }
  },
  components: {

    "emoji-picker": emoji
  },
  mounted () {
    
      
  },
  methods:{
    get_user(){
       const config = {
    method: "GET",
    headers: {
      'content-type': 'application/json',
      'X-CSRFToken': CSRF_TOKEN
    }
    }
      axios
      .get('/api/user/',config)
      .then(response => (this.currentuser = response.data))
      // console.log(this.currentuser)
    },
    
    get_users(user){
      this.selected=user
      const config = {
    method: "GET",
    headers: {
      'content-type': 'application/json',
      'X-CSRFToken': CSRF_TOKEN
    }
    }
    axios
      .get('/api/get_users/',config)
      .then(response => (this.users=response.data))
      let index=this.users.indexOf(this.currentuser);
      this.users.splice(index,1);
      // console.log(this.users)
    },
    get_chat(user){
      this.selected=user;
    var endpoint='/Status/message/?search='+this.currentuser.username+'+'+user;
    console.log(endpoint)
     const config = {
    method: "GET",
    headers: {
      'content-type': 'application/json',
      'X-CSRFToken': CSRF_TOKEN
    }
    }
      axios
      .get(endpoint,config)
      .then(response => (this.messages=response.data))
      let div = document.getElementById('accordion');

//make the last element (a message) to scroll into view, smoothly!
div.lastElementChild.scrollIntoView({ behavior: 'smooth' });
      // console.log(this.messages)
    }
    
    
  },
  created(){
      this.get_user();
      this.get_users();
      // console.log(this.users)
    }
  
};

</script>
<style scoped>
h1,h2,h3,h4,h5,button{
  font: italic small-caps bold 20px/30px Georgia, serif;
}
img {
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 5px;
  width: 50px;
}

img:hover {
  box-shadow: 0 0 2px 1px rgba(0, 140, 186, 0.5);
}
.container{
  padding: 10px;
}
.scrolluser {
  height:100%;
  overflow-y: scroll;
}
</style>
