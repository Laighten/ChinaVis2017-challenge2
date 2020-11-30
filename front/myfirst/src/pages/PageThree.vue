<template>
    <div id=PageThree>
      <div class="wrap">
      <div class="content container">
        <h3 class="page-title">
          illegal
          <small>illegalBar and illegalPeople Data</small>
        </h3>
        <div class="row">
            <div class="col-lg-4">
                <section class="widget">
                <T-one/>
                </section>
            </div>
            <div class="col-lg-8">
                <section class="widget">
                <T-two/>
                </section>
            </div>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
import TableOne from '../components/TableOne'
import TableTwo from '../components/TableTwo';
export default {
    components:{
        'T-one':TableOne,
        'T-two':TableTwo
    },
    data(){
        return {}
    }
}
</script>

<style>
.PageThree {
  height: 100%;
  position: relative;
}
</style>