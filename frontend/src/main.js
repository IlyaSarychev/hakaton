import Vue from 'vue';

import App from './App.vue';
import router from './router';
import store from './store';
import SortedTablePlugin from "vue-sorted-table";

Vue.use(SortedTablePlugin);

Vue.config.productionTip = false;

export default new Vue({
    router,
    store,
    el: '#app',
    template: '<App/>',
    components: { App },
});