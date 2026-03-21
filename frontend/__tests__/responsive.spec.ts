import { test, expect } from '@playwright/test';

test.describe('Responsive Design', () => {
  test('should render correctly on mobile (320px)', async ({ page }) => {
    await page.setViewportSize({ width: 320, height: 640 });
    await page.goto('http://localhost:3004', { waitUntil: 'networkidle' });

    // Check that display is visible
    const display = page.locator('[data-testid="display"]');
    await expect(display).toBeVisible();

    // Check that buttons are visible
    const buttons = page.locator('button');
    const buttonCount = await buttons.count();
    expect(buttonCount).toBeGreaterThan(10);

    // Check that calculator doesn't overflow
    const calculatorWrapper = page.locator('.calculator-wrapper');
    const boundingBox = await calculatorWrapper.boundingBox();
    expect(boundingBox).not.toBeNull();
    if (boundingBox) {
      expect(boundingBox.width).toBeLessThanOrEqual(320);
    }
  });

  test('should render correctly on tablet (768px)', async ({ page }) => {
    await page.setViewportSize({ width: 768, height: 1024 });
    await page.goto('http://localhost:3004', { waitUntil: 'networkidle' });

    // Check that display is visible
    const display = page.locator('[data-testid="display"]');
    await expect(display).toBeVisible();

    // Check that all buttons are visible
    const buttons = page.locator('button');
    const buttonCount = await buttons.count();
    expect(buttonCount).toBeGreaterThan(10);

    // Verify calculator is centered
    const calculatorWrapper = page.locator('.calculator-wrapper');
    await expect(calculatorWrapper).toBeVisible();
  });

  test('should render correctly on desktop (1024px)', async ({ page }) => {
    await page.setViewportSize({ width: 1024, height: 768 });
    await page.goto('http://localhost:3004', { waitUntil: 'networkidle' });

    // Check that display is visible
    const display = page.locator('[data-testid="display"]');
    await expect(display).toBeVisible();

    // Check that all buttons are visible
    const buttons = page.locator('button');
    const buttonCount = await buttons.count();
    expect(buttonCount).toBeGreaterThan(10);

    // Verify grid layout
    const buttonsGrid = page.locator('.buttons-grid');
    await expect(buttonsGrid).toBeVisible();
  });

  test('should render correctly on wide desktop (1920px)', async ({ page }) => {
    await page.setViewportSize({ width: 1920, height: 1080 });
    await page.goto('http://localhost:3004', { waitUntil: 'networkidle' });

    // Check that display is visible
    const display = page.locator('[data-testid="display"]');
    await expect(display).toBeVisible();

    // Check that all buttons are visible
    const buttons = page.locator('button');
    const buttonCount = await buttons.count();
    expect(buttonCount).toBeGreaterThan(10);

    // Verify calculator is still centered and not too large
    const calculator = page.locator('.calculator');
    const boundingBox = await calculator.boundingBox();
    expect(boundingBox).not.toBeNull();
    if (boundingBox) {
      expect(boundingBox.width).toBeLessThanOrEqual(500);
    }
  });

  test('should maintain functionality on mobile', async ({ page }) => {
    await page.setViewportSize({ width: 320, height: 640 });
    await page.goto('http://localhost:3004', { waitUntil: 'networkidle' });

    // Click 5
    await page.locator('[data-testid="button-5"]').click();
    // Click +
    await page.locator('[data-testid="add"]').click();
    // Click 3
    await page.locator('[data-testid="button-3"]').click();
    // Click =
    await page.locator('[data-testid="equals"]').click();
    // Wait for response
    await page.waitForTimeout(500);

    // Verify result is displayed
    const display = page.locator('[data-testid="display"]');
    const displayText = await display.textContent();
    expect(displayText).toContain('8');
  });

  test('should maintain functionality on tablet', async ({ page }) => {
    await page.setViewportSize({ width: 768, height: 1024 });
    await page.goto('http://localhost:3004', { waitUntil: 'networkidle' });

    // Click 6
    await page.locator('[data-testid="button-6"]').click();
    // Click ×
    await page.locator('[data-testid="multiply"]').click();
    // Click 2
    await page.locator('[data-testid="button-2"]').click();
    // Click =
    await page.locator('[data-testid="equals"]').click();
    // Wait for response
    await page.waitForTimeout(500);

    // Verify result is displayed
    const display = page.locator('[data-testid="display"]');
    const displayText = await display.textContent();
    expect(displayText).toContain('12');
  });

  test('should maintain functionality on desktop', async ({ page }) => {
    await page.setViewportSize({ width: 1024, height: 768 });
    await page.goto('http://localhost:3004', { waitUntil: 'networkidle' });

    // Click 9
    await page.locator('[data-testid="button-9"]').click();
    // Click ÷
    await page.locator('[data-testid="divide"]').click();
    // Click 3
    await page.locator('[data-testid="button-3"]').click();
    // Click =
    await page.locator('[data-testid="equals"]').click();
    // Wait for response
    await page.waitForTimeout(500);

    // Verify result is displayed
    const display = page.locator('[data-testid="display"]');
    const displayText = await display.textContent();
    expect(displayText).toContain('3');
  });

  test('buttons should be properly sized on mobile', async ({ page }) => {
    await page.setViewportSize({ width: 320, height: 640 });
    await page.goto('http://localhost:3004', { waitUntil: 'networkidle' });

    // Get button size
    const button = page.locator('[data-testid="button-5"]');
    const boundingBox = await button.boundingBox();
    expect(boundingBox).not.toBeNull();
    if (boundingBox) {
      // Buttons should be at least 40px tall
      expect(boundingBox.height).toBeGreaterThanOrEqual(40);
      // Buttons should not be too wide
      expect(boundingBox.width).toBeLessThan(100);
    }
  });

  test('text should be readable on all sizes', async ({ page }) => {
    const viewportSizes = [
      { width: 320, height: 640 },
      { width: 768, height: 1024 },
      { width: 1024, height: 768 },
      { width: 1920, height: 1080 },
    ];

    for (const size of viewportSizes) {
      await page.setViewportSize(size);
      await page.goto('http://localhost:3004', { waitUntil: 'networkidle' });

      // Check that header is visible
      const header = page.locator('h1');
      await expect(header).toBeVisible();

      // Check that it's not cut off
      const headerBox = await header.boundingBox();
      expect(headerBox).not.toBeNull();
      if (headerBox) {
        expect(headerBox.y).toBeGreaterThanOrEqual(0);
      }
    }
  });
});
