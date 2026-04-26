#!/usr/bin/env bash
# Convert all biomarker MDs to PDFs, using md2pdf template with fallback to plain pandoc
set -uo pipefail

MD2PDF="/c/Users/rwa/.claude/skills/md2pdf/md2pdf.sh"

for md in outputs/*.md; do
  name=$(basename "$md" .md)
  [[ "$name" == *provenance* || "$name" == *plan* ]] && continue
  pdf="papers/${name}.pdf"
  [ -f "$pdf" ] && continue  # skip already converted
  
  echo "=== Converting: $name ==="
  if bash "$MD2PDF" "$md" "$pdf" "Biomarker Sheet" 2>/dev/null; then
    echo "  OK (template)"
  else
    echo "  Template failed, using plain pandoc..."
    pandoc "$md" -o "$pdf" --pdf-engine=xelatex -V geometry:margin=2.5cm -V fontsize=11pt -V mainfont="Cambria" 2>/dev/null
    if [ -f "$pdf" ]; then
      echo "  OK (plain)"
    else
      echo "  FAILED"
    fi
  fi
done

echo ""
echo "=== PDF Status ==="
ls -1 papers/*.pdf 2>/dev/null | wc -l
echo "PDFs generated"
