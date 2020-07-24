<template>
    <div class="container">

        <h1 class="text-center text-uppercase">Profile </h1>
        <div class="row justify-center-md-center" >
                 <div class="col-md-6 offset-md-3">
                <b-img v-bind="mainProps" id='profile' src="https://picsum.photos/250/250/?image=58" rounded="circle" alt="Circle image"></b-img>
                 </div>
        </div>
        <div class="row justify-center-md-center" id='menu'>
                 <div class="col-md-6 offset-md-3">
                    <div class="mt-3">
                    <b-button-group size="lg">
                    <b-button variant="light"><b-icon-images class="h5 mb-2"></b-icon-images></b-button>
                    <b-button variant="light"><b-icon-info-square class="h5 mb-2"></b-icon-info-square></b-button>
                    <b-button variant="light"><b-icon-shield-shaded class="h5 mb-2"></b-icon-shield-shaded></b-button>
                    </b-button-group>
                    </div>
                </div>
        </div>
        <div class="row justify-center-md-center" >
                 <div class="col-md-6 offset-md-3">
                            <ul class="list-group">
                    <li class="list-group-item ">
                        <div class="md-v-line"></div><i class="fas fa-laptop mr-4 pr-3"></i> Cras justo odio
                    </li>
                    <li class="list-group-item">
                        <div class="md-v-line"></div><i class="fas fa-bomb mr-5"></i>Dapibus ac facilisis in
                    </li>
                    <li class="list-group-item">
                        <div class="md-v-line"></div><i class="fas fa-code mr-5"></i>Morbi leo risus
                    </li>
                    <li class="list-group-item">
                        <div class="md-v-line"></div><i class="far fa-gem mr-5"></i>Porta ac consectetur ac
                    </li>
                    <li class="list-group-item">
                        <div class="md-v-line"></div><i class="fas fa-cogs mr-5"></i>Vestibulum at eros
                    </li>
                    </ul>
                 </div>
        </div>
    <div class="row justify-content-md-center">
            
                <div class="row">
                        <ul class="nav nav-tabs" id="myTab" role="tablist">
                            <li class="nav-item">
                                <a class="nav-link active" id="home-tab" data-toggle="tab" href="#home" role="tab" aria-controls="home" aria-selected="true">About</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" id="profile-tab" data-toggle="tab" href="#profile" role="tab" aria-controls="profile" aria-selected="false">Timeline</a>
                            </li>
                        </ul>
                </div>
                <div class="row">
                    <div class="tab-content profile-tab" id="myTabContent">
                                    <div class="tab-pane fade show active" id="home" role="tabpanel" aria-labelledby="home-tab">
                                                <div class="row">
                                                    <div class="col">
                                                        <label>User Id</label>
                                                    </div>
                                                    <div class="col">
                                                        <p>{{ userdata.id}}</p>
                                                    </div>
                                                </div>
                                                <div class="row">
                                                    <div class="col">
                                                        <label>Name</label>
                                                    </div>
                                                    <div class="col">
                                                        <p>{{userdata.username}}</p>
                                                    </div>
                                                </div>
                                                <div class="row">
                                                    <div class="col">
                                                        <label>First name</label>
                                                    </div>
                                                    <div class="col">
                                                        <div v-if="editmode===true">
                                                        <b-form-input  id="input-small"  v-model='f_name' size="sm" :placeholder="userdata.first_name"></b-form-input>
                                                        <br>
                                                        </div>
                                                        <div v-else>
                                                    
                                                        <p>{{ userdata.first_name}}</p>
                                                    </div>
                                                </div>
                                                </div>
                                                <div class="row">
                                                    <div class="col">
                                                        <label>Last name</label>
                                                    </div>
                                                    <div class="col" >
                                                                    <div v-if="editmode===true">
                                                                    <b-form-input  id="input-small" v-model='l_name' size="sm" :placeholder="userdata.last_name"></b-form-input>
                                                                    <br>
                                                                    </div>
                                                                    <div v-else>
                                                                
                                                                    <p>{{ userdata.last_name}}</p>
                                                                    </div>
                                                    </div>
                                                </div>
                                                <div class="row">
                                                    <div class="col">
                                                        <label>Email</label>
                                                    </div>
                                                    <div class="col">
                                                        <div v-if="editmode===true">
                                                        <b-form-input  id="input-small" v-model="email" size="sm" :placeholder="userdata.email"></b-form-input>
                                                        <br>
                                                        </div>
                                                        <div v-else>
                                                    
                                                        <p>{{ userdata.email}}</p>
                                                    </div>
                                                </div>
                                                </div>
                                                <div class="row">
                                                    <div class="col">
                                                        <label>Phone</label>
                                                    </div>
                                                    <div class="col">
                                                        <p>123 456 7890</p>
                                                    </div>
                                                </div>
                                                <div class="row">
                                                    <div class="col">
                                                        <label>Profession</label>
                                                    </div>
                                                    <div class="col">
                                                        <p>Web Developer and Designer</p>
                                                    </div>
                                                </div>
                                    </div>
                                    <div class="tab-pane fade" id="profile" role="tabpanel" aria-labelledby="profile-tab">
                                                <div class="row">
                                                    <div class="col">
                                                        <label>Active now</label>
                                                    </div>
                                                    <div class="col">
                                                        <p>{{ userdata.is_active}}</p>
                                                    </div>
                                                </div>
                                                <div class="row">
                                                    <div class="col">
                                                        <label>Staff</label>
                                                    </div>
                                                    <div class="col">
                                                        <p>{{ userdata.is_staff}}</p>
                                                    </div>
                                                </div>
                                                <div class="row">
                                                    <div class="col">
                                                        <label>Date Joined</label>
                                                    </div>
                                                    <div class="col-8">
                                                        <p>{{userdata.date_joined}}</p>
                                                    </div>
                                                </div>
                                                <div class="row">
                                                    <div class="col-md-12">
                                                        <label>Your Bio</label><br/>
                                                        <p>Your detail description</p>
                                                    </div>
                                                </div>
                                    
                                </div>
            

            </div>
             <div class="column">
                <div v-if="editmode===true">
                    <div v-ripple.mouseover="'rgba(66,109,109, 0.35)'" v-on:click='edit_form' class="button is-primary is-large"  style="margin: 1rem,width:3in">Save</div>
                </div>
                <div v-else>
                    <div v-ripple.mouseover="'rgba(66,109,109, 0.35)'" v-on:click='edit_form_initiate' class="button is-primary is-large"  style="margin: 1rem, width:3in">Edit profile</div>
                </div>

                
            </div>
            </div>
    </div>
     <!-- <img v-bind:src="currentuser.image" alt="huh"/> -->
    
   
                    
</div>
</template>
<script>
import axios from 'axios';
// import emoji from "@/components/emoji.vue";
import { CSRF_TOKEN } from "@/common/csrftoken.js"

export default {
    data(){
    return{
    editmode:false,
    imageeditmode:false,
    placeholder:'',
    file:null,
    email:'',
    l_name:'',
    f_name:'',
    currentuser:'',
    userdata:'',
    msg: "Vue Image Upload and Resize Demo",
    previewImage:null,
    mainProps: {  width: 175, height: 175, class: 'm1' }
    
    }
  },
  watch:{
    editmode:function(){
        this.get_user_data();
    }

  },
   methods:{
       uploadImage(e){
                const image = e.target.files[0];
                const reader = new FileReader();
                reader.readAsDataURL(image);
                reader.onload = e =>{
                    this.previewImage = e.target.result;
                    console.log(this.previewImage);
                }
       },
    get_profile(){
       const config = {
    method: "GET",
    headers: {
      'content-type': 'application/json',
      'X-CSRFToken': CSRF_TOKEN
    }
    }
      axios
      .get('/api/profile/',config)
      .then(response => (this.currentuser = response.data))
      console.log(this.currentuser)
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
      .then(response => (this.userdata = response.data))
    },



    getImageUrl() {
        return this.currentuser.image
      },


    edit_form_initiate(){
        this.editmode=true;
        this.email=this.userdata.email;
      this.l_name=this.userdata.last_name;
      this.f_name=this.userdata.first_name;
    },
    image_edit_initiate(){
        this.imageeditmode=true;
    },

    image_edit(){
         const user=this.currentuser.id;
                const config = {
                headers: {
                'content-type': 'application/json',
                'X-CSRFToken': CSRF_TOKEN
                }
                }
                var endpoint='api/profile/'+user;
                console.log(endpoint)
                axios
                .put(endpoint,{
                        'image':this.previewImage,
                    },config)
                .then((response) => {
                                        console.log(response);
                                        }, (error) => {
                                        console.log(error);
                                        });
                            this.imageeditmode=false;
                        
       
    },
    edit_form(){
                const user=this.userdata.id;
                const config = {
                headers: {
                'content-type': 'application/json',
                'X-CSRFToken': CSRF_TOKEN
                }
                }
                var endpoint='/api/user/'+user;
                console.log(endpoint)
                axios
                .put(endpoint,{
                        'email':this.email,
                        'last_name':this.l_name,
                        'first_name':this.f_name
                    },config)
                .then((response) => {
                                        console.log(response);
                                        }, (error) => {
                                        console.log(error);
                                        });
                            this.editmode=false;
                            this.get_user_data();
                           
       }
       
    
},
created(){
      
      this.get_user_data();
      this.get_profile();
    },
}
</script>
<style scoped>
body{
    background: -webkit-linear-gradient(left, #3931af, #00c6ff);
}
.emp-profile{
    padding: 3%;
    margin-top: 3%;
    margin-bottom: 3%;
    border-radius: 0.5rem;
    background: #fff;
}
.profile-img{
    text-align: center;
}

.profile-img .file {
    position: relative;
    overflow: hidden;
    margin-top: -20%;
    width: 70%;
    border: none;
    border-radius: 0;
    font-size: 15px;
    background: #212529b8;
}
.profile-img .file input {
    position: absolute;
    opacity: 0;
    right: 0;
    top: 0;
}
.profile-head h5{
    color: #333;
}
.profile-head h6{
    color: #0062cc;
}
.profile-edit-btn{
    border: none;
    border-radius: 1.5rem;
    width: 70%;
    padding: 2%;
    font-weight: 600;
    color: #6c757d;
    cursor: pointer;
}
.proile-rating{
    font-size: 12px;
    color: #818182;
    margin-top: 5%;
}
.proile-rating span{
    color: #495057;
    font-size: 15px;
    font-weight: 600;
}
.profile-head .nav-tabs{
    margin-bottom:5%;
}
.profile-head .nav-tabs .nav-link{
    font-weight:600;
    border: none;
}
.profile-head .nav-tabs .nav-link.active{
    border: none;
    border-bottom:2px solid #0062cc;
}
.profile-work{
    padding: 14%;
    margin-top: -15%;
}
.profile-work p{
    font-size: 12px;
    color: #818182;
    font-weight: 600;
    margin-top: 10%;
}
.profile-work a{
    text-decoration: none;
    color: #495057;
    font-weight: 600;
    font-size: 14px;
}
.profile-work ul{
    list-style: none;
}
.profile-tab label{
    font-weight: 600;
}
.profile-tab p{
    font-weight: 600;
    height: 10px;
    color: #0062cc;
}
#myTabContent{
    height: 500px;
    padding-top: 0.5in;
}
#myTabContent .row{
    padding-top: 0.1in;
}
#myTabContent p{
    width: 100%;
}
.container{
    padding-top:0.2in;
}
.column button{
    width: 2in;
}
#card{
    height: 500px;
}
.row{
    padding-top:0.2in;
}
#menu{
    border-bottom: 1px solid black;
}
#profile{
    /* border: 3px dotted  #0062cc; */
}
</style>