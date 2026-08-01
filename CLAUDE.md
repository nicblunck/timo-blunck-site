# Timo Blunck — Website

Dies ist die Website von Timo Blunck (Autor & Musiker), ursprünglich in Webflow
gebaut, jetzt als einfache Code-Website. Sie besteht nur aus HTML-Dateien, einer
CSS-Datei und Bildern — **keine Datenbank, kein Build-Schritt, nichts Kompliziertes.**

Design von Nicolas Blunck. Fotos von Kai Heimberg.

---

## Für Timo: So aktualisierst du die Seite

Du musst **nichts** über Programmieren wissen. Sag mir (Claude) einfach in normalen
Worten, was du ändern möchtest, zum Beispiel:

- „Ändere auf der Startseite den Text über das neue Album.“
- „Tausche das Portraitfoto gegen das neue Bild aus, das ich dir gebe.“
- „Füge auf der Presse-Seite ein neues Zitat hinzu: ›…‹ von XY.“
- „Der Erscheinungstermin hat sich geändert — überall 19.6. statt 20.6.“
- „Mach den Link zum Emons-Buch aktuell, hier ist die neue Adresse: …“

Ich kümmere mich darum, **welche** Datei geändert werden muss und ob ein Bild im
HTML oder im CSS hinterlegt ist. Du musst das nicht wissen.

### Ein neues Foto verwenden
1. Leg die Bilddatei in den Ordner `assets/images/` (oder gib sie mir im Chat).
2. Sag mir, **welches** Bild ersetzt werden soll („das große Portrait oben auf der
   About-Seite“). Ich erledige den Rest.
3. Tipp: Fotos vorher nicht zu riesig machen (lange Seite ≈ 2000 Pixel reicht),
   sonst lädt die Seite langsam. Wenn du unsicher bist, gib mir das Originalfoto —
   ich kann es verkleinern.

### Veröffentlichen (live schalten)
Nachdem ich etwas geändert habe, sag einfach **„Bitte veröffentliche die Änderungen“**.
→ Siehe Abschnitt *Veröffentlichen* weiter unten.

---

## Die Seiten

| Datei            | Seite      | Inhalt                                              |
|------------------|------------|-----------------------------------------------------|
| `index.html`     | Startseite | Aktuelles, neues Buch & Album, Zitate, Videos       |
| `about.html`     | About      | Biografie, Portraitfoto                             |
| `bucher.html`    | Bücher     | Alle Bücher mit Beschreibungen und Kauf-Links       |
| `musik.html`     | Musik      | Alben/Diskografie                                   |
| `live.html`      | Live       | Termine / Auftritte                                 |
| `presse.html`    | Presse     | Pressestimmen, Fotos                                |
| `impressum.html` | Impressum  | Rechtliche Angaben                                  |

Die Navigation (Menü oben) ist auf jeder Seite gleich. Wenn eine Seite umbenannt
oder hinzugefügt wird, muss das Menü auf **allen** Seiten angepasst werden — das
mache ich automatisch, sag mir einfach Bescheid.

## Wo was liegt (für Neugierige)

- `*.html` — die einzelnen Seiten. Der sichtbare Text steht direkt im HTML.
- `assets/css/style.css` — das gesamte Aussehen (Schrift, Farben, Layout,
  Hintergrundbilder). **Hier besser nichts von Hand ändern** — das Design ist fein
  abgestimmt. Bitte mich, wenn etwas anders aussehen soll.
- `assets/images/` — alle Bilder.
- `assets/js/` — Technik für Animationen/Menü (nicht anfassen).

## Schriftarten

Die Schriften liegen jetzt **lokal auf der Seite selbst** (selbst gehostet,
`assets/fonts/` + `assets/css/fonts.css`) — es gibt **keine Abhängigkeit von Adobe
Fonts / Typekit mehr**. Dadurch werden sie auf jeder Internet-Adresse korrekt
angezeigt, ohne dass irgendwo eine Domain freigeschaltet werden muss.

Verwendet werden frei lizenzierte Ersatzschriften für die ursprünglichen
Webflow/Adobe-Schriften:

- **Montserrat** statt gill-sans-nova (Fließtext, Überschriften, Titel)
- **Jost** statt futura-pt (Buttons)
- **Courier Prime** statt courier-std (Zitate)

## Videos

Die Videos liegen bei **Vimeo** und werden nur eingebettet. Um ein Video
auszutauschen, brauche ich nur den neuen Vimeo-Link.

---

## Veröffentlichen (Hosting)

Die Seite liegt auf **GitHub** (`nicblunck/timo-blunck-site`) und wird über
**Vercel** gehostet. Vercel ist mit dem GitHub-Repo verbunden: Jeder `git push`
auf den `main`-Branch löst automatisch eine neue Veröffentlichung aus (meist
innerhalb von ~30 Sekunden online).

Das heißt für Claude: Nach einer Änderung reicht `git add` + `git commit` +
`git push`, damit die Änderung live geht — kein separater Deploy-Schritt nötig.

### Wenn Timo selbst mit eigenem Claude arbeitet

Timo kann diese Seite auch von seinem eigenen Rechner mit seinem eigenen Claude
Code bearbeiten (statt Änderungen über Nicolas laufen zu lassen). Voraussetzung:

1. Ein GitHub-Account für Timo mit Schreibrechten (Collaborator) auf
   `nicblunck/timo-blunck-site`.
2. Claude Code auf seinem Rechner installiert und mit einem lokalen Klon des
   Repos verbunden.

Diese `CLAUDE.md` liegt im Repo und gilt dann automatisch auch für sein Claude —
er kann genau wie Nicolas in normalen Worten sagen, was geändert werden soll,
und danach „Bitte veröffentliche die Änderungen" sagen. Claude committet und
pusht direkt auf `main`; es gibt keinen Review-Zwischenschritt.

## Vorschau auf dem eigenen Rechner

Um die Seite lokal anzuschauen, ohne sie zu veröffentlichen, kann Claude einen
kleinen Vorschau-Server starten (`python3 .claude/serve.py`, dann
`http://127.0.0.1:4321` im Browser öffnen). Frag mich einfach: „Zeig mir die Seite
in der Vorschau.“

---

## Hinweise für Claude (technisch)

- Statische Site, kein Build. Aus dem Webflow-Export lokalisiert: CSS/JS/Bilder
  liegen lokal unter `assets/`, alle CDN-URLs wurden umgeschrieben.
- Interne Links sind relative `.html`-Pfade (`href="about.html"`). Beim Anlegen
  einer neuen Seite das Navigationsmenü in **allen** `*.html` aktualisieren.
- Bilder sind teils `<img src>`, teils CSS-`background-image` in `style.css`. Beim
  Bildtausch prüfen, ob der Dateiname im HTML oder im CSS referenziert wird (am
  einfachsten: gleicher Dateiname → Datei in `assets/images/` ersetzen).
- `style.css` ist generiertes Webflow-CSS mit kryptischen Klassennamen — mit Vorsicht
  bearbeiten; für reine Inhalts-/Bildänderungen nicht nötig.
- Externe Links (Spotify, Amazon, Emons, Tapete, Dussmann, Vimeo) bleiben
  extern und sind beabsichtigt.
- Schriften sind selbst gehostet (`assets/css/fonts.css`, `assets/fonts/`). Kein
  Typekit/Adobe-Loader mehr — beim Bearbeiten keine Adobe-CDN-URLs wieder einfügen.
