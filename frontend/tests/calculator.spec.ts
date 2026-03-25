import { test, expect } from '@playwright/test';

test.describe('Pac-Man Arcade Calculator', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/');
    // Wait for calculator to load
    await page.waitForSelector('.pacman-calculator');
  });

  test('should display initial state with 0', async ({ page }) => {
    const display = page.locator('.pacman-display .value');
    await expect(display).toContainText('0');
  });

  test('should perform basic addition (5 + 3 = 8)', async ({ page }) => {
    await page.click('button:has-text("5")');
    await page.click('button:has-text("+")');
    await page.click('button:has-text("3")');
    await page.click('button:has-text("=")');

    const display = page.locator('.pacman-display .value');
    await expect(display).toContainText('8');
  });

  test('should perform basic subtraction (10 - 4 = 6)', async ({ page }) => {
    await page.click('button:has-text("1")');
    await page.click('button:has-text("0")');
    await page.click('button:has-text("−")');
    await page.click('button:has-text("4")');
    await page.click('button:has-text("=")');

    const display = page.locator('.pacman-display .value');
    await expect(display).toContainText('6');
  });

  test('should perform basic multiplication (6 * 7 = 42)', async ({ page }) => {
    await page.click('button:has-text("6")');
    await page.click('button:has-text("×")');
    await page.click('button:has-text("7")');
    await page.click('button:has-text("=")');

    const display = page.locator('.pacman-display .value');
    await expect(display).toContainText('42');
  });

  test('should perform basic division (20 / 4 = 5)', async ({ page }) => {
    await page.click('button:has-text("2")');
    await page.click('button:has-text("0")');
    await page.click('button:has-text("/")');
    await page.click('button:has-text("4")');
    await page.click('button:has-text("=")');

    const display = page.locator('.pacman-display .value');
    await expect(display).toContainText('5');
  });

  test('should clear calculator on C button', async ({ page }) => {
    await page.click('button:has-text("5")');
    await page.click('button:has-text("+")');
    await page.click('button:has-text("3")');
    await page.click('button:has-text("C")');

    const display = page.locator('.pacman-display .value');
    await expect(display).toContainText('0');
  });

  test('should handle decimal input (3.14)', async ({ page }) => {
    await page.click('button:has-text("3")');
    await page.click('button:has-text(".")');
    await page.click('button:has-text("1")');
    await page.click('button:has-text("4")');

    const display = page.locator('.pacman-display .value');
    await expect(display).toContainText('3.14');
  });

  test('should toggle scientific mode', async ({ page }) => {
    // Initially in standard mode
    let buttons = page.locator('button');
    const initialCount = await buttons.count();

    // Click SCI button
    await page.click('button:has-text("SCI")');

    // Scientific buttons should be visible
    const sqrtButton = page.locator('button:has-text("√")');
    await expect(sqrtButton).toBeVisible();

    // Click STD button to toggle back
    await page.click('button:has-text("STD")');

    // Scientific buttons should be hidden
    await expect(sqrtButton).not.toBeVisible();
  });

  test('should have arcade theme elements', async ({ page }) => {
    // Check for Pac-Man themed display
    const display = page.locator('.pacman-display');
    await expect(display).toBeVisible();

    // Check for score display
    const scoreText = page.locator('.pacman-display .score');
    await expect(scoreText).toBeVisible();

    // Check for level display
    const levelText = page.locator('.pacman-display:has-text("LEVEL")');
    await expect(levelText).toBeVisible();

    // Check for arcade buttons
    const arcadeButtons = page.locator('.arcade-button');
    const buttonCount = await arcadeButtons.count();
    expect(buttonCount).toBeGreaterThan(0);
  });

  test('should display ghosts in arcade theme', async ({ page }) => {
    // Check for ghost elements
    const ghosts = page.locator('.ghost');
    const ghostCount = await ghosts.count();
    expect(ghostCount).toBeGreaterThan(0);
  });

  test('should display Pac-Man icon', async ({ page }) => {
    const pacmanIcon = page.locator('.pacman-icon');
    await expect(pacmanIcon).toBeVisible();
  });

  test('scientific sqrt operation (√16 = 4)', async ({ page }) => {
    // Toggle to scientific mode
    await page.click('button:has-text("SCI")');

    // Enter 16
    await page.click('button:has-text("1")');
    await page.click('button:has-text("6")');

    // Click sqrt button
    await page.click('button:has-text("√")');

    const display = page.locator('.pacman-display .value');
    await expect(display).toContainText('4');
  });

  test('should be responsive on mobile', async ({ page }) => {
    // Set mobile viewport
    await page.setViewportSize({ width: 375, height: 667 });

    // Calculator should still be visible
    const calculator = page.locator('.pacman-calculator');
    await expect(calculator).toBeVisible();

    // Should be able to perform calculation
    await page.click('button:has-text("2")');
    await page.click('button:has-text("+")');
    await page.click('button:has-text("3")');
    await page.click('button:has-text("=")');

    const display = page.locator('.pacman-display .value');
    await expect(display).toContainText('5');
  });
});
