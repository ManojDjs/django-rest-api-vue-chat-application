<template>
  <div>
    <div class="container">
        <form @submit.prevent="onSubmit">
            <div class="form-group">
                <input type="file" @change="onFileUpload">
            </div>
            <div class="form-group">
                <input type="text" v-model="name" placeholder="Name" class="form-control">
            </div>
            <div class="form-group">
                <button class="btn btn-primary btn-block btn-lg">Upload File</button>
            </div>
        </form>
    </div>    
  </div>
</template>

<script>
import axios from "axios";
// import axios from 'axios';
// import emoji from "@/components/emoji.vue";
import { CSRF_TOKEN } from "@/common/csrftoken.js"

export default {
  data() {
      return {
         FILE: null,
         name: ''
      };
    },
    methods: {
        onFileUpload (event) {
          this.FILE = event.target.files[0]
        },
        onSubmit() {
          // upload file
          const formData = new FormData()
          formData.append('image', this.FILE, this.FILE.name)
          formData.append('Content', this.name)
          formData.append('likes',[4])
          const config = {
            headers: {
            'content-type': 'multipart/form-data',
            'X-CSRFToken': CSRF_TOKEN
            }}
          axios.post('http://localhost:8000/Status/status/', formData, config).then((res) => {
            console.log(res)
          })
        }  
    }

}
</script>

<style scoped >
.container {
  max-width: 600px;
}
</style>