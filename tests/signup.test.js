'use strict'
import puppeteer from 'puppeteer';
import faker from 'faker';
const app = 'http://127.0.0.1:5500/UI/user/signup.html';
const leadData = {
    firstname: 'brian',
    lastname: 'ogutu',
    password: 'Pod#23@A',
    confirmpassword: 'Pod#23@A',
    email: faker.internet.email(),
    username: faker.name.firstName(),
    phoneNumber: '+254703812914'
};
let page;
let browser;
const width = 1920;
const height = 1080;
beforeAll(async () => {
    browser = await puppeteer.launch({
        headless: true,
        // slowMo: 80,
        // args: [`--window-size=${width},${height}`]
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
        await page.goto(app);
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
        // page.on('dialog',dialog=>{
        //     expect(dialog.message()).toEqual("Signedup")
        // })
    }, 1600000);
});