import type { Metadata } from 'next';
import { Providers } from './providers';
import '../styles/globals.scss';

export const metadata: Metadata = {
  title: 'Pac-Man Arcade Calculator',
  description: 'A retro arcade-themed calculator with Pac-Man aesthetics',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        <Providers>{children}</Providers>
      </body>
    </html>
  );
}
