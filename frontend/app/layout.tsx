import type { Metadata } from "next";
import "./globals.scss";

export const metadata: Metadata = {
  title: "Stranger Things Calculator",
  description: "A themed calculator with animations",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
