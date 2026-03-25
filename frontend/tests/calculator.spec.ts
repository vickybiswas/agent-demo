import { test, expect } from "@playwright/test";

test.describe("Calculator", (): void => {
  test("should perform addition: 5 + 3 = 8", async ({
    page,
  }): Promise<void> => {
    await page.goto("/");

    await page.click('button:has-text("5")');
    await page.click('button:has-text("+")');
    await page.click('button:has-text("3")');
    await page.click('button:has-text("=")');

    const display = page.locator("p");
    await expect(display.last()).toContainText("8");
  });

  test("should perform subtraction: 10 - 3 = 7", async ({
    page,
  }): Promise<void> => {
    await page.goto("/");
    await page.click('button:has-text("C")'); // Clear

    await page.click('button:has-text("1")');
    await page.click('button:has-text("0")');
    await page.click('button:has-text("-")');
    await page.click('button:has-text("3")');
    await page.click('button:has-text("=")');

    const display = page.locator("p");
    await expect(display.last()).toContainText("7");
  });

  test("should perform multiplication: 4 * 5 = 20", async ({
    page,
  }): Promise<void> => {
    await page.goto("/");
    await page.click('button:has-text("C")');

    await page.click('button:has-text("4")');
    await page.click('button:has-text("*")');
    await page.click('button:has-text("5")');
    await page.click('button:has-text("=")');

    const display = page.locator("p");
    await expect(display.last()).toContainText("20");
  });

  test("should perform division: 20 / 4 = 5", async ({
    page,
  }): Promise<void> => {
    await page.goto("/");
    await page.click('button:has-text("C")');

    await page.click('button:has-text("2")');
    await page.click('button:has-text("0")');
    await page.click('button:has-text("/")');
    await page.click('button:has-text("4")');
    await page.click('button:has-text("=")');

    const display = page.locator("p");
    await expect(display.last()).toContainText("5");
  });

  test("should clear on C button", async ({ page }): Promise<void> => {
    await page.goto("/");

    await page.click('button:has-text("5")');
    await page.click('button:has-text("C")');

    const display = page.locator("p");
    await expect(display.last()).toContainText("0");
  });
});
