//Contains urls to various pages and api links
const urls = {
    signupUrl: 'http://127.0.0.1:5000/api/v2/auth/signup',
    loginUrl: 'http://127.0.0.1:5000/api/v2/auth/login',
    postMeetupUrl: 'http://127.0.0.1:5000/api/v2/meetups',
    postQuestionUrl: 'http://127.0.0.1:5000/api/v2/questions',
    commentUrl: 'http://127.0.0.1:5000/api/v2/comments/',
    logoutUrl: 'http://127.0.0.1:5000/api/v2/auth/logout'
}
const pageUrls = {
    signupPage: 'http://127.0.0.1:5500/UI/user/signup.html',
    loginPage: 'http://127.0.0.1:5500/UI/user/login.html',
    indexpage: 'http://127.0.0.1:5500/UI/index.html',
    createMeetupPage: 'http://127.0.0.1:5500/UI/user/meetupform.html',
    postQuestionPage: 'http://127.0.0.1:5500/UI/user/question.html',
    commentsPage: 'http://127.0.0.1:5500/UI/user/questionview.html'
}
export {
    urls,
    pageUrls,
};