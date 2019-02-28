'use strict'
//tests for the functionality of the signup page
import puppeteer from 'puppeteer';
import faker from 'faker';
import {
    pageUrls
} from '../UI/js/urls.js';
const signupPage = pageUrls.signupPage;
const loginPage = pageUrls.loginPage;
const indexPage = pageUrls.indexpage;
const meetupForm = pageUrls.createMeetupPage;
const leadData = {
    firstname: 'brian',
    lastname: 'ogutu',
    password: 'Pod#23@A',
    confirmpassword: 'Pod#23@A',
    email: faker.internet.email(),
    username: faker.name.firstName(),
    phoneNumber: '+254703812914',
    location: faker.lorem.word(),
    topic: faker.commerce.productName(),
    happeningOn: '24-08-2019',
    body: faker.lorem.text()
};
//jest.setTimeout(30000);
const adminData = {
    email: 'admin@gmail.com',
    password: 'password12#B'
}
let page;
let browser;
const width = 1920;
const height = 1080;
beforeAll(async () => {
    browser = await puppeteer.launch({
        headless: false
    })
    page = await browser.newPage();
    await page.setViewport({
        width,
        height
    });
});
afterAll(() => {
    browser.close();
});
describe('signup form', () => {
    test('Submit signup request', async () => {
        await page.goto(signupPage);
        await page.waitForSelector('#signupForm');
        await page.click('input[id=firstname]');
        await page.type('input[id=firstname]', leadData.firstname);
        await page.click('input[id=lastname]');
        await page.type('input[id=lastname]', leadData.lastname);
        await page.click('input[id=phoneNumber]');
        await page.type('input[id=phoneNumber', leadData.phoneNumber);
        await page.click('input[id=password]');
        await page.type('input[id=password]', leadData.password);
        await page.click('input[id=username]');
        await page.type('input[id=username]', leadData.username);
        await page.click('input[id=confirmpassword]');
        await page.type('input[id=confirmpassword]', leadData.confirmpassword);
        await page.click('input[id=email]');
        await page.type('input[id=email]', leadData.email);
        await page.click('button[id=postSignUp]');
    });
});
describe("Login Form", () => {
    test("A user with an account can log in", async () => {
        await page.goto(loginPage);
        await page.waitForSelector('#login-form');
        await page.click('input[id=email]');
        await page.type('input[id=email]', adminData.email);
        await page.click('input[id=password]');
        await page.type('input[id=password]', adminData.password);
        await page.click('button[id=loginButton]');
    });
});
describe("Login Form", () => {
    test("A user with an account can log in", async () => {
        await page.goto(indexPage);
        await page.waitForSelector('#login-form');
        await page.click('input[id=email]');
        await page.type('input[id=email]', leadData.email);
        await page.click('input[id=password]');
        await page.type('input[id=password]', leadData.password);
        await page.click('button[id=loginButton]');
    });
});
describe("Login as an admin and create meetup", () => {
    test("An admin should be able to create meetup", async () => {
        await page.goto(meetupForm);
        await page.waitForSelector('#meetup-form');
        await page.click('input[id=location]');
        await page.type('input[id=location]', leadData.location);
        await page.click('input[id=topic]');
        await page.type('input[id=topic]', leadData.topic);
        await page.click('input[id=happeningOn]');
        await page.type('input[id=happeningOn]', leadData.happeningOn);
        await page.click('textarea[id=body]');
        await page.type('textarea[id=body]', leadData.body);
        await page.click('button[id=postMeeup]');
    });
});