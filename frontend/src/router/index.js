import Vue from 'vue';
import Router from 'vue-router';
import Home from '@/views/Home'
import Login from '@/views/Login';
import Lost from '@/views/Lost';
import Register from '@/views/Register';
import VerifyEmail from '@/views/VerifyEmail';
import Table from '@/views/Table';

import store from '../store';

const requireAuthenticated = (to, from, next) => {
    store.dispatch('auth/initialize')
        .then(() => {
            if (!store.getters['auth/isAuthenticated']) {
                next('/login');
            } else {
                next();
            }
        });
};

const requireUnauthenticated = (to, from, next) => {
    store.dispatch('auth/initialize')
        .then(() => {
            if (store.getters['auth/isAuthenticated']) {
                next('/home');
            } else {
                next();
            }
        });
};

const redirectLogout = (to, from, next) => {
    store.dispatch('auth/logout')
        .then(() => next('/login'));
};

Vue.use(Router);

export default new Router({
    saveScrollPosition: true,
    routes: [{
            path: '/home',
            component: Home,
            beforeEnter: requireAuthenticated,
        },
        {
            path: '/',
            redirect: '/home',
        },
        {
            path: '/register',
            component: Register,
        },
        {
            path: '/register/:key',
            component: VerifyEmail,
        },
        {
            path: '/login',
            component: Login,
            beforeEnter: requireUnauthenticated,
        },
        {
            path: '/logout',
            beforeEnter: redirectLogout,
        },
        {
            path: '/table',
            component: Table,
            beforeEnter: requireUnauthenticated,
        },
        {
            path: '*',
            component: Lost
        },
    ],
});