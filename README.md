# Davis Bellan Ltd — website

Single-page landing site. The background is a generative WebGL artwork grown from
the real coastline and street network of Portsmouth, UK. A new random seed is drawn
on every page load, so the tide lines, coastal fronds and street veins are unique
each visit, and then move gently.

## Files

| Path | Purpose |
| --- | --- |
| `index.html` | The deployable page. Fully self-contained (map data embedded); only external request is Google Fonts. |
| `src/template.html` | Editable source with a `__DATA__` placeholder for the map. |
| `src/portsmouth.json` | Simplified, projected OSM geometry (coastline + streets). |
| `src/build.py` | Rebuilds `index.html` from the template and data. |

## Editing

Edit `src/template.html`, then run:

```sh
python3 src/build.py
```

## Hosting

Any static host works. For GitHub Pages: **Settings → Pages → Deploy from a branch → `main` / root**.

## Map data

Coastline and streets © [OpenStreetMap contributors](https://www.openstreetmap.org/copyright),
available under the Open Database License (ODbL). The on-page attribution line must stay.
Bounding box 50.765–50.860 N, 1.165–1.005 W.
