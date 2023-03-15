# Prise en Main 

## 1)

Cette typologie s'appelle client-serveur ou étoile

## 2)

On remarque dans les logs que l'on peut voir qui a écrit un message et surtout le message qui a été envoyé. 

## 3 )

Le problème est que avec ses logs sont que tous les massages sont stockées en clair dans les logs, cela viole le principe de confidentialité des données. Cela viole le principe de Kerckhoffs car la sécurité du serveur ne repose pas sur une clé de chiffrement 

## 4)

Pour éviter que les logs ne soient révélés, ils faudraient chiffrer les messages de bout en bout pour les messages échangés entre les clients et le serveur comme le fait WhatsApp. Pouyr cela, il faudrait chiffrer le message avant qu'il ne soit envoyé sur le réseau et le déchiffrer qu'à l'arriver.
