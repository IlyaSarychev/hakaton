<template>
   <div id="activate-account-view">
      <h1>Подтверждение аккаунта</h1>
      <template v-if="activationLoading">загрузка...</template>
      <template v-else-if="activationError">Произошла ошибка.</template>
      <template v-else-if="activationCompleted">
         Активация аккаунта прошла успешно.
         <router-link v-if="!isAuthenticated" to="/login">
            Нажмите, чтобы войти.
         </router-link>
      </template>
   </div>
</template>

<script>
import {
   mapActions,
   mapGetters,
   mapState,
} from 'vuex'

export default {
   computed: {
      ...mapGetters('auth', ['isAuthenticated']),
      ...mapState('signup', [
         'activationCompleted',
         'activationError',
         'activationLoading',
      ]),
   },
   methods: mapActions('signup', [
      'activateAccount',
      'clearActivationStatus',
   ]),
   created() {
      this.activateAccount(this.$route.params);
   },
   beforeRouteLeave(to, from, next) {
      this.clearActivationStatus();
      next();
   },
}
</script>