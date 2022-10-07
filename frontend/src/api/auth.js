import session from './session';

export default {
    login(username, password) {
        return session.post('/auth/login/', { username, password });
    },
    logout() {
        return session.post('/auth/logout/', {});
    },
    createAccount(lastName, name, patronymic, inn, company, post, email, phone, password, confirmPassword) {
        return session.post('/registration/', { lastName, name, patronymic, inn, company, post, email, phone, password, confirmPassword });
    },

    getAccountDetails() {
        return session.get('/auth/user/');
    },
    updateAccountDetails(data) {
        return session.patch('/auth/user/', data);
    },
    verifyAccountEmail(key) {
        return session.post('/registration/verify-email/', { key });
    },
};