<template>
  <div id='app'>
    <div v-show="isLightOFF" class="light-off"></div> 

    <app-header class="header"></app-header>
    
    <div class="container-fluid">
        <!-- 左侧栏 -->
        <nav id="sidebar" class="sidebar nav-collapse collapse">
            <ul id="side-nav" class="side-nav">
              <h3 class="page-title">Select<small> DashBorad</small></h3>
              <section class="widget large">
                <li class="active">
                    <router-link to="/Test">
                    <i class="fa fa-cog"></i> <span class="name">Geographical</span>
                    </router-link>
                </li>
                 <li class="active">
                    <router-link to="/page2">
                    <i class="fa fa-tree"></i> <span class="name">AgeTime</span>
                    </router-link>
                </li>
                <li class="active">
                    <router-link to="/PageThree">
                    <i class="fa fa-folder-open"></i> <span class="name">illegalBar </span>
                    </router-link>
                </li>
                 <li class="active">
                    <router-link to="/PageFour">
                    <i class="fa fa-magic"></i> <span class="name">Signature </span>
                    </router-link>
                </li>
              </section>
            </ul>
        </nav> 
        <!--  -->

        <!-- <test/> -->
        <router-view/>
    </div>
    
    
    <app-footer class="footer"></app-footer>
  </div>
</template>

<script>
import Test from './pages/Test'

import appHeader from './components/common/Header'
import appFooter from './components/common/Footer'
import page2 from './pages/page2'
import PageThree from './pages/PageThree'


export default {
  name: 'App',
  components:{
    appHeader,
    Test,
    page2,
    PageThree,
    appFooter,
  

  },
  data() {
    return {
      isLightOFF: false
    }
  },
  mounted() {
    this.$root.Bus.$on('lightOFF', (params) => {
      this.isLightOFF = params
    })
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0;
  position: relative;
}
.container-fluid {
  height: 95%;
}
.header{
  box-sizing:border-box;
  height: 3%;
}
.footer{
  box-sizing:border-box;
  height:2%
}
.light-off {
  margin: 0;
  padding: 0;
  position: absolute;
  top:0 ;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0,0,0,0.6);
  z-index: 100
}
</style>
