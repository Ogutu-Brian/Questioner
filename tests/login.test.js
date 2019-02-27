'use strict'
///tests for functionality of the login page
import puppeteer from 'puppeteer';
import {
    pageUrls
} from '../UI/js/urls.js';
import {
    leadData
} from './signup.test.js';
const app = pageUrls.loginPage;
let page;
let browser;
const width = 1920;
const height = 1080;
beforeAll(async () => {
    browser = await puppeteer.launch({
        headless: true
    });
    page = await browser.newPage();
    await page.setViewport({
        width,
        height
    });
});
afterAll(() => {
    browser.close();
});
describe("Login Form", () => {
    test("A user with an account can log in", async () => {
        await page.goto(app);
        await page.waitForSelector('#login-form');
        await page.click('input[id=email]');
        await page.type('input[id=email]', leadData.email);
        await page.click('input[id=password]');
        await page.type('input[id=password]', leadData.password);
        await page.click('button[id=loginButton]');
    }, 160000);
});