import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import logout from '@/components/logout.vue';
import Profile from '@/components/profile.vue';
import HW from '@/components/HelloWorld.vue';
Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/",
    name: "Logout",
    component: logout
  },
  {
    path: "/hw",
    name: "hw",
    component: HW
  },
  {
    path: "/profile",
    name: "profie",
    component: Profile
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue")
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
