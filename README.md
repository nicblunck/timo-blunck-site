# Timo Blunck — Website

Live: **[timoblunck.com](https://timoblunck.com)**

Die Website von Timo Blunck (Autor & Musiker). Ursprünglich in Webflow gebaut,
mittlerweile eine einfache Code-Website: nur HTML-Dateien, eine CSS-Datei und
Bilder — keine Datenbank, kein Build-Schritt, kein CMS.

Design von Nicolas Blunck. Fotos von Kai Heimberg.

## Bearbeiten

Diese Seite wird nicht per Hand im Code bearbeitet, sondern per Gespräch mit
Claude — auf Deutsch, in normalen Worten, z. B. „Ändere auf der Startseite den
Text über das neue Album." Alle Details dazu (welche Datei was enthält, wie
Bilder ausgetauscht werden, wie veröffentlicht wird) stehen in
[`CLAUDE.md`](CLAUDE.md).

## Seiten

| Datei            | Seite      | Inhalt                                        |
|------------------|------------|------------------------------------------------|
| `index.html`     | Startseite | Aktuelles, neues Buch & Album, Zitate, Videos  |
| `about.html`     | About      | Biografie, Portraitfoto                        |
| `bucher.html`    | Bücher     | Alle Bücher mit Beschreibungen und Kauf-Links  |
| `musik.html`     | Musik      | Alben/Diskografie                              |
| `live.html`      | Live       | Termine / Auftritte                            |
| `presse.html`    | Presse     | Pressestimmen, Fotos                           |
| `impressum.html` | Impressum  | Rechtliche Angaben                             |

## Struktur

```
├── *.html              einzelne Seiten, sichtbarer Text direkt im HTML
├── assets/css/         Aussehen (Schrift, Farben, Layout)
├── assets/fonts/       selbst gehostete Schriften (kein Adobe/Typekit)
├── assets/images/      Bilder
└── assets/js/          Animationen/Menü
```

## Hosting & Veröffentlichen

Gehostet auf **Vercel**, verbunden mit diesem GitHub-Repo. Jeder Push auf
`main` veröffentlicht die Seite automatisch (in der Regel < 30 Sekunden).

## Lokale Vorschau

```bash
python3 .claude/serve.py
```

Dann `http://127.0.0.1:4321` im Browser öffnen.
