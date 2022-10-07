<template>
   <div id="register-view">
      <h1>Регистрация</h1>
      <template v-if="registrationLoading">
         загрузка...
      </template>
      <template v-else-if="!registrationCompleted">
         <form @submit.prevent="submit">
            <input v-model="inputs.lastName" type="text" id="lastName" placeholder="Фамилия" />
            <input v-model="inputs.name" type="text" id="name" placeholder="Имя" />
            <input v-model="inputs.patronymic" type="text" id="patronymic" placeholder="Отчество" />
            <input v-model="inputs.inn" type="number" id="inn" placeholder="Инн" />
            <input v-model="inputs.company" type="text" id="company" placeholder="Название компании">
            <input v-model="inputs.post" type="text" id="post" placeholder="Должность">
            <input v-model="inputs.email" type="email" id="email" placeholder="Электронная почта">
            <input v-model="inputs.phone" type="number" id="phone" placeholder="Телефон">
            <input v-model="inputs.password" type="password" id="password" placeholder="Пароль">
            <input v-model="inputs.confirmPassword" type="password" id="confirmPassword" placeholder="Подтверждение">
         </form>
         <button @click="createAccount(inputs)">
            Создать
         </button>
         <span class="error" v-show="registrationError">
            При обработке вашего запроса произошла ошибка.
         </span>
         <div>
            Уже есть аккаунт?
            <router-link to="/login">Войти</router-link> |
            <!-- <router-link to="/password_reset">reset password</router-link> -->
         </div>
      </template>
      <template v-else>
         <div>
            Регистрация завершена. Вскоре вы должны получить письмо на электронную почту о том, как активировать свою
            учётную запись.
         </div>
         <div>
            <router-link to="/login">Вернуться на странице авторизации</router-link>
         </div>
      </template>
   </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'

export default {
   data() {
      return {
         inputs: {
            lastName: "",
            name: "",
            patronymic: "",
            inn: "",
            company: "",
            post: "",
            email: "",
            phone: "",
            password: "",
            confirmPassword: "",
         },
      };
   },
   computed: mapState('signup', [
      'registrationCompleted',
      'registrationError',
      'registrationLoading',
   ]),
   methods: mapActions('signup', [
      'createAccount',
      'clearRegistrationStatus',
   ]),
   beforeRouteLeave(to, from, next) {
      this.clearRegistrationStatus();
      next();
   },
};
</script>

<style>
form input {
   display: block
}

.error {
   color: crimson;
   font-size: 12px;
}
</style>