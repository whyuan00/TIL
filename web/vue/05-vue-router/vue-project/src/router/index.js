import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import UserView from '@/views/UserView.vue'
import UserPosts from '@/components/UserPosts.vue';
import UserProfile from '@/components/UserProfile.vue';
import LoginView from '@/views/LoginView.vue'


const isAuthenticated = true


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited
      //c 초기 로딩 너무 오래걸리지 않게 하기 위해 나중에로드.
      component: () => import('../views/AboutView.vue')
    },
    {
      // view는 시작슬래시 필요 
      path:'/user/:id',
      name: 'user',
      component: UserView,
      // 특정 라우트 안에 작성
      beforeEnter: ((to,from)=> {
        // console.log(to)
      }),

      children:[
        {
          path:'profile', name:'user-profile',component: UserProfile
        },
        {
          path:'posts', name:'user-posts',component: UserPosts
        }
      ]



    },
    {
      path:'/login',
      name:'login',
      component: LoginView,
      beforeEnter: (to, from)=>{
        if (isAuthenticated ===true){
          console.log('이미로그인')
        }
        return {name: home}
      }      
    }
  ]
})
// 전역가드/ 제일 마지막에 작성
// 어디론가 이동하기 직전에 항상 자동호출
// router.beforeEach((to,from) =>{
//   // 로그인 안한 사용자는 이동시마다 로그인 페이지로 redirect
//   const isAuthenticated = false

//   if (!isAuthenticated && to.name !== 'login') {
//     console.log('로그인하세요')
//     return {name:'login'}
//   }

// })

export default router
