<template>
  <div class="hello">

    <h2>Пользователи</h2>

    <ul>
        <li v-for="user in users" v-bind:key="user.username">{{user}}</li>
    </ul>

  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'HelloWorld',
  data() {
    return {
      users: []
    }
  },
  methods: {
    async fetchUsers() {
        try {
          const response = await axios.get('http://localhost:8000/users/');
          this.users = response.data;
        } catch (error) {
          console.log(error);
        }
    }
  },
  created() {
    this.fetchUsers();
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
