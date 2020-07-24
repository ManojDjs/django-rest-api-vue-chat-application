<template>
  <div class="container">
    <div class="row justify-center-md-center" >
    <div class="col-md-6 offset-md-3"  v-for="(post,index) in posts"
                  v-bind:key="index" >
          <!-- Card -->
                   
                  <div class="card">
                    <!-- Card image -->
                    <div class='row justify-content-start' id='card_user'>
                    <b-img v-bind="mainProps" id='profile' src="https://picsum.photos/250/250/?image=58" rounded="circle" alt="Circle image"></b-img>
                   
                    <h5 class="user_name">{{post.author}}</h5>
                    </div>
                    <div class="view overlay">
                      <b-img class="card-img-top" v-bind='mainPropscard' :src="post.image" alt="Card image cap"/>
                              <a>
                                <div class="mask rgba-white-slight"></div>
                              </a>
                    </div>
                    
                    <!-- Button -->
                    <a class="btn-floating btn-action ml-auto mr-4 mdb-color lighten-3"><i
                        class="fas fa-chevron-right pl-1"></i></a>
                    <!-- Card content -->
                    
                    <!-- Card footer -->
                    <div class="rounded-bottom mdb-color lighten-3  pt-0">
                      <ul class="list-unstyled list-inline font-small">
                        <!-- <li class="list-inline-item pr-2 white-text"><i class="far fa-clock pr-1"></i>05/10/2015</li> -->
                        <button type="button" @click='like(post.slug)' class="btn btn-light">{{post.likes_post}}<b-icon-hand-thumbs-up class="h5 mb-2" variant="primary"></b-icon-hand-thumbs-up></button>
                        <button type="button" class="btn btn-light"><b-icon-chat-quote class="h5 mb-2" variant="primary"></b-icon-chat-quote></button>
                        <!-- <button type="button" class="btn btn-light"><b-icon-hand-thumbs-up class="h3 mb-2" variant="primary"></b-icon-hand-thumbs-up></button> -->
                      </ul>
                      <hr>
                    </div>
                    <div class="card-body">
                      <!-- Title -->
                      <h4 class="card-title">{{post.Content}}</h4>
                      <p>{{post.created_at}}</p>
                      
                      </div>
               </div>
                 </div>

</div>
<!-- Card -->

  </div>
</template>
<script>
import axios from 'axios';
// import emoji from "@/components/emoji.vue";
import { CSRF_TOKEN } from "@/common/csrftoken.js"
export default {
  data(){
    return{
      posts:[],
       mainProps: {  width: 40, height: 40, class: 'm1' },
       mainPropscard:{ class: 'm1'},
       user_data:'',
       like_mode:false,
    }
  },
  watch:{
    like_mode:function(){
        this.get_profile();
        this.like_mode=false;
    }
  },
methods:
{
  get_profile(){
       const config = {
    method: "GET",
    headers: {
      'content-type': 'application/json',
      'X-CSRFToken': CSRF_TOKEN
    }
    }
      axios
      .get('/Status/status/',config)
      .then(response => (this.posts = response.data))
      console.log(this.posts)
    },
    like(slug){
      
       const config = {
    method: "GET",
    headers: {
      'content-type': 'application/json',
      'X-CSRFToken': CSRF_TOKEN
    }
    }
      axios
      .post('/Status/status/'+slug+'/like',{likes:[this.user_data.username]},config)
      this.like_mode=true;
    },
    get_user_data(){
        const config = {
    method: "GET",
    headers: {
      'content-type': 'application/json',
      'X-CSRFToken': CSRF_TOKEN
    }
    }
      axios
      .get('/api/user/',config)
      .then(response => (this.user_data = response.data))
    },
},
created(){
  this.get_profile();
}
}
</script>
<style scoped>
.card{
  /* height: 5in; */
  width: 5in;
}
#card_user{
  padding-left: 0.2in;
  padding-top: 0.2in;
  padding-bottom: 0.1in;
}
.user_name{
  padding-top:0.1in;
  padding-left: 0.1in;
}
</style>