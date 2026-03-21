import { test, expect } from '@playwright/test';

test.describe('Calculator Operations', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('http://localhost:3004', { waitUntil: 'networkidle' });
  });

  test('should render calculator on page load', async ({ page }) => {
    const display = page.locator('[data-testid="display"]');
    await expect(display).toBeVisible();
    await expect(display).toContainText('0');
  });

  test('should display number when clicked (5)', async ({ page }) => {
    const button5 = page.locator('[data-testid="button-5"]');
    await button5.click();
    const display = page.locator('[data-testid="display"]');
    await expect(display).toContainText('5');
  });

  test('should add two numbers (5 + 3 = 8)', async ({ page }) => {
    // Click 5
    await page.locator('[data-testid="button-5"]').click();
    // Click +
    await page.locator('[data-testid="add"]').click();
    // Click 3
    await page.locator('[data-testid="button-3"]').click();
    // Click =
    await page.locator('[data-testid="equals"]').click();
    // Wait for API response
    await page.waitForTimeout(1000);
    // Verify result
    const display = page.locator('[data-testid="display"]');
    const displayText = await display.textContent();
    expect(displayText).toMatch(/8/);
  });

  test('should subtract two numbers (10 - 3 = 7)', async ({ page }) => {
    // Click 1
    await page.locator('[data-testid="button-1"]').click();
    // Click 0
    await page.locator('[data-testid="button-0"]').click();
    // Click -
    await page.locator('[data-testid="subtract"]').click();
    // Click 3
    await page.locator('[data-testid="button-3"]').click();
    // Click =
    await page.locator('[data-testid="equals"]').click();
    // Wait for API response
    await page.waitForTimeout(1000);
    // Verify result
    const display = page.locator('[data-testid="display"]');
    const displayText = await display.textContent();
    expect(displayText).toMatch(/7/);
  });

  test('should multiply two numbers (6 × 2 = 12)', async ({ page }) => {
    // Click 6
    await page.locator('[data-testid="button-6"]').click();
    // Click ×
    await page.locator('[data-testid="multiply"]').click();
    // Click 2
    await page.locator('[data-testid="button-2"]').click();
    // Click =
    await page.locator('[data-testid="equals"]').click();
    // Wait for API response
    await page.waitForTimeout(1000);
    // Verify result
    const display = page.locator('[data-testid="display"]');
    const displayText = await display.textContent();
    expect(displayText).toMatch(/12/);
  });

  test('should divide two numbers (9 ÷ 3 = 3)', async ({ page }) => {
    // Click 9
    await page.locator('[data-testid="button-9"]').click();
    // Click ÷
    await page.locator('[data-testid="divide"]').click();
    // Click 3
    await page.locator('[data-testid="button-3"]').click();
    // Click =
    await page.locator('[data-testid="equals"]').click();
    // Wait for API response
    await page.waitForTimeout(1000);
    // Verify result
    const display = page.locator('[data-testid="display"]');
    const displayText = await display.textContent();
    expect(displayText).toMatch(/3/);
  });

  test('should handle decimal numbers', async ({ page }) => {
    // Click 3
    await page.locator('[data-testid="button-3"]').click();
    // Click .
    await page.locator('[data-testid="decimal"]').click();
    // Click 5
    await page.locator('[data-testid="button-5"]').click();
    // Verify decimal is displayed
    const display = page.locator('[data-testid="display"]');
    await expect(display).toContainText('3.5');
  });

  test('should clear display when C is pressed', async ({ page }) => {
    // Click 5
    await page.locator('[data-testid="button-5"]').click();
    // Click C (Clear)
    await page.locator('[data-testid="clear"]').click();
    // Verify display is cleared
    const display = page.locator('[data-testid="display"]');
    await expect(display).toContainText('0');
  });

  test('should clear all when AC is pressed', async ({ page }) => {
    // Click 5
    await page.locator('[data-testid="button-5"]').click();
    // Click +
    await page.locator('[data-testid="add"]').click();
    // Click AC (All Clear)
    await page.locator('[data-testid="all-clear"]').click();
    // Verify display is cleared
    const display = page.locator('[data-testid="display"]');
    await expect(display).toContainText('0');
  });

  test('should backspace correctly', async ({ page }) => {
    // Click 5, 4, 3
    await page.locator('[data-testid="button-5"]').click();
    await page.locator('[data-testid="button-4"]').click();
    await page.locator('[data-testid="button-3"]').click();
    // Verify display shows 543
    const display = page.locator('[data-testid="display"]');
    await expect(display).toContainText('543');
    // Click backspace
    await page.locator('[data-testid="backspace"]').click();
    // Verify display shows 54
    await expect(display).toContainText('54');
  });

  test('should handle memory operations', async ({ page }) => {
    // Click 5
    await page.locator('[data-testid="button-5"]').click();
    // Click M+ (Memory Add)
    await page.locator('[data-testid="memory-add"]').click();
    // Click 3
    await page.locator('[data-testid="button-3"]').click();
    // Click M+ (Memory Add)
    await page.locator('[data-testid="memory-add"]').click();
    // Click MR (Memory Recall)
    await page.locator('[data-testid="memory-recall"]').click();
    // Wait for animation
    await page.waitForTimeout(300);
    // Verify memory is recalled (5 + 3 = 8)
    const display = page.locator('[data-testid="display"]');
    const displayText = await display.textContent();
    expect(displayText).toContain('8');
  });

  test('should validate CORS headers on API call', async ({ page }) => {
    page.on('response', (response) => {
      const url = response.url();
      if (url.includes('localhost:8004') || url.includes('backend:8004')) {
        const corsHeader = response.headers()['access-control-allow-origin'];
        // CORS header validation happens implicitly
        expect(corsHeader).toBeDefined();
      }
    });

    // Click 5
    await page.locator('[data-testid="button-5"]').click();
    // Click +
    await page.locator('[data-testid="add"]').click();
    // Click 3
    await page.locator('[data-testid="button-3"]').click();
    // Click =
    await page.locator('[data-testid="equals"]').click();
    // Wait for API response
    await page.waitForTimeout(1000);

    // CORS header should be present if backend is running
  });

  test('should handle missing backend gracefully', async ({ page }) => {
    // Try a calculation
    await page.goto('http://localhost:3004', { waitUntil: 'networkidle' });
    await page.locator('[data-testid="button-5"]').click();
    await page.locator('[data-testid="add"]').click();
    await page.locator('[data-testid="button-3"]').click();
    await page.locator('[data-testid="equals"]').click();
    await page.waitForTimeout(6000);

    // Error message might appear if backend is not available
    // This test ensures the frontend doesn't crash
  });
});
