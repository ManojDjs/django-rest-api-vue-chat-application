<template>
  <div id="exampleInputEmoji">
    <div class="your-input-box">
      <!-- {{ currentuser}}
      {{ selected }} -->
      <input type="text" class="form-control" v-model="valueInput" />
      <button @click="toogleDialogEmoji">😃</button>
    </div>
    <button class="btn btn-outline-primary" @click='wrap'>send message</button>
    <VEmojiPicker v-show="showDialog" 
    :style="{width:500}"
    labelSearch="Search"
     lang="pt-BR" 
     @select="onSelectEmoji" />
  </div>
</template>

<script>
import VEmojiPicker, { emojisDefault, categoriesDefault } from "v-emoji-picker";
import axios from 'axios';
import { CSRF_TOKEN } from "@/common/csrftoken.js"
export default {
  props:{
    'messages':[String],
    'selected':String,
    'currentuser':String,
    'get_chat':Function
    }
    ,
  name: "exampleInputEmoji",
  components: {
    VEmojiPicker
  },
  data: () => ({
    valueInput: "",
    showDialog: false,
    selecteduser:''
  }),
  mounted() {
    console.log(categoriesDefault);
    console.log("Total emojis:", emojisDefault.length);
  },
  methods: {
    toogleDialogEmoji() {
      console.log(this.showDialog);
      this.showDialog = !this.showDialog;
      console.log(this.showDialog);
    },
    onSelectEmoji(emoji) {
      console.log(this.showDialog);
        if (this.showDialog==true){
        console.log(emoji.data);
         console.log(this.selected);
        this.valueInput += emoji.data;
      // this.$emit("selectedemoji", this.valueInput);
      }
      // Optional
      // this.toogleDialogEmoji();
    },
    wrap(){
       this.$emit("selectedemoji", this.valueInput);
       const config = {
        headers: {
        'content-type': 'application/json',
        'X-CSRFToken': CSRF_TOKEN
        }
        }
    axios
      .post('/Status/message/',{
            'text':this.valueInput,
            'sender':this.currentuser,
            'receiver':this.selected
        },config)
      .then((response) => {
                            console.log(response);
                            }, (error) => {
                            console.log(error);
                            });
       this.valueInput='';
       this.$emit('get_chat');
       this.$parent.get_chat(this.selected);
       if (this.showDialog==true){
       this.showDialog=!this.showDialog;
       }
       }
    }
  
};
</script>

<style lang="css" scoped>
#exampleInputEmoji {
  position: relative;
}

.your-input-box {
  display: flex;
  align-items: center;
  justify-content: center;
}

input {
  padding: 8px;
  font-size: 16px;
  margin-right: 2px;
  border-radius: 4px;
  border: 1px solid #848484;
}

button {
  border-radius: 4px;
  padding: 5px;
  font-size: 22px;
  border: 1px solid #848484;
}
</style>