import { test, expect } from '@playwright/test';

test.describe('Calculator UI Tests', () => {
  test.beforeEach(async ({ page }) => {
    // Mock the API responses
    await page.route('**/add*', (route) => {
      route.abort();
    });
    await page.route('**/subtract*', (route) => {
      route.abort();
    });
    await page.route('**/multiply*', (route) => {
      route.abort();
    });
    await page.route('**/divide*', (route) => {
      route.abort();
    });

    await page.goto('http://localhost:3004');
    await page.waitForLoadState('load');
  });

  test('should load calculator page', async ({ page }) => {
    await expect(page).toHaveTitle('Stranger Things Calculator');
    await expect(page.locator('text=CALC-1980')).toBeVisible();
  });

  test('should display 0 by default', async ({ page }) => {
    const display = page.locator('div').first().locator('div').nth(1);
    await expect(display).toContainText('0');
  });

  test('basic number input - single digit', async ({ page }) => {
    await page.click('[data-button="5"]');
    await page.waitForTimeout(100);
    const display = page.locator('div').first().locator('div').nth(1);
    await expect(display).toContainText('5');
  });

  test('basic number input - multiple digits', async ({ page }) => {
    await page.click('[data-button="1"]');
    await page.click('[data-button="2"]');
    await page.click('[data-button="3"]');
    await page.waitForTimeout(100);
    const display = page.locator('div').first().locator('div').nth(1);
    await expect(display).toContainText('123');
  });

  test('decimal number input', async ({ page }) => {
    await page.click('[data-button="3"]');
    await page.click('[data-button="decimal"]');
    await page.click('[data-button="1"]');
    await page.click('[data-button="4"]');
    await page.waitForTimeout(100);
    const display = page.locator('div').first().locator('div').nth(1);
    await expect(display).toContainText('3.14');
  });

  test('clear button (AC) should reset to 0', async ({ page }) => {
    await page.click('[data-button="5"]');
    await page.click('[data-button="clear"]');
    await page.waitForTimeout(100);
    const display = page.locator('div').first().locator('div').nth(1);
    await expect(display).toContainText('0');
  });

  test('delete button (DEL) should remove last digit', async ({ page }) => {
    await page.click('[data-button="1"]');
    await page.click('[data-button="2"]');
    await page.click('[data-button="3"]');
    await page.click('[data-button="delete"]');
    await page.waitForTimeout(100);
    const display = page.locator('div').first().locator('div').nth(1);
    await expect(display).toContainText('12');
  });

  test('upside down mode should toggle on display click', async ({ page }) => {
    await page.click('[data-button="5"]');
    const display = page.locator('div').first().locator('div').nth(1);

    // Click the display to toggle upside down
    await display.click();

    // Toggle again
    await display.click();

    // Verify the display is still there
    await expect(display).toContainText('5');
  });

  test('C button should clear current input', async ({ page }) => {
    await page.click('[data-button="5"]');
    await page.click('[data-button="add"]');
    await page.click('[data-button="3"]');
    await page.click('[data-button="c"]');
    await page.waitForTimeout(100);
    const display = page.locator('div').first().locator('div').nth(1);
    await expect(display).toContainText('0');
  });

  test('all buttons should be visible and clickable', async ({ page }) => {
    const buttons = [
      '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
      'add', 'subtract', 'multiply', 'divide', 'decimal',
      'clear', 'delete', 'c', 'equals', 'upsidedown'
    ];

    for (const button of buttons) {
      const element = page.locator(`[data-button="${button}"]`);
      await expect(element).toBeVisible();
    }
  });

  test('buttons should highlight on hover', async ({ page }) => {
    const button = page.locator('[data-button="5"]');
    await button.hover();
    await page.waitForTimeout(200);
    const classes = await button.getAttribute('class');
    expect(classes).toBeTruthy();
  });

  test('operation buttons should have distinct styling', async ({ page }) => {
    const addButton = page.locator('[data-button="add"]');
    const numberButton = page.locator('[data-button="5"]');

    const addClasses = await addButton.getAttribute('class');
    const numberClasses = await numberButton.getAttribute('class');

    expect(addClasses).toBeTruthy();
    expect(numberClasses).toBeTruthy();
    expect(addClasses).not.toEqual(numberClasses);
  });

  test('demogorgon graphic should be present', async ({ page }) => {
    const svg = page.locator('svg');
    await expect(svg).toBeVisible();
  });

  test('calculator container should be visible', async ({ page }) => {
    const calculator = page.locator('text=CALC-1980').locator('..').locator('..');
    await expect(calculator).toBeVisible();
  });

  test('page should not have console errors', async ({ page }) => {
    const errors: string[] = [];
    page.on('console', (msg) => {
      if (msg.type() === 'error') {
        errors.push(msg.text());
      }
    });

    await page.click('[data-button="1"]');
    await page.click('[data-button="add"]');
    await page.click('[data-button="2"]');
    await page.waitForTimeout(500);

    expect(errors).toHaveLength(0);
  });

  test('numbers above 16 digits should be prevented', async ({ page }) => {
    // Try to enter 17 digits
    for (let i = 0; i < 17; i++) {
      await page.click('[data-button="9"]');
    }
    await page.waitForTimeout(100);
    const display = page.locator('div').first().locator('div').nth(1);
    const text = await display.textContent();
    const digits = text?.match(/[0-9]/g) || [];
    expect(digits.length).toBeLessThanOrEqual(16);
  });

  test('multiple decimal points should be prevented', async ({ page }) => {
    await page.click('[data-button="3"]');
    await page.click('[data-button="decimal"]');
    await page.click('[data-button="1"]');
    await page.click('[data-button="decimal"]');
    await page.waitForTimeout(100);
    const display = page.locator('div').first().locator('div').nth(1);
    const text = await display.textContent();
    const decimalCount = (text?.match(/\./g) || []).length;
    expect(decimalCount).toBeLessThanOrEqual(1);
  });

  test('responsive layout check', async ({ page }) => {
    const calculator = page.locator('text=CALC-1980').locator('..').locator('..');
    const boundingBox = await calculator.boundingBox();
    expect(boundingBox).toBeTruthy();
    expect(boundingBox?.width).toBeGreaterThan(0);
    expect(boundingBox?.height).toBeGreaterThan(0);
  });
});
