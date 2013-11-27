#!/bin/bash

PYGMENTIZE=`which pygmentize`
TEMPFILE=/tmp/dotbydotgraphics-output.tex

rm -fr $TEMPFILE

cat >> $TEMPFILE <<EOF
\documentclass[document.tex]{subfiles}
\begin{document}
\section{Source codes}
EOF

for filename in $( wc `find ./dotbydotgraphics* -name "*.py" -print` | awk '$1 > 7 {print $4;}' | grep dotbydot --color=never );
do
cat >> $TEMPFILE <<EOF
\subsection{$( echo $filename | sed 's/_/\\_/g' )}
\fontsize{10pt}{12pt}\selectfont
EOF
$PYGMENTIZE -f latex -l python -O linenos $filename | grep -v "copyright" >> $TEMPFILE
done

cat >> $TEMPFILE <<EOF
\end{document}
EOF

cat $TEMPFILE
rm -fr $TEMPFILE
