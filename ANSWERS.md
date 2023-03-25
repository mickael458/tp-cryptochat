# Prise en Main 

## 1)

Cette typologie s'appelle client-serveur ou étoile

## 2)

On remarque dans les logs que l'on peut voir qui a écrit un message et surtout le message qui a été envoyé. 

## 3 )

Le problème est que avec ses logs sont que tous les massages sont stockées en clair dans les logs, cela viole le principe de confidentialité des données. Cela viole le principe de Kerckhoffs car la sécurité du serveur ne repose pas sur une clé de chiffrement 

## 4)

Pour éviter que les logs ne soient révélés, ils faudraient chiffrer les messages de bout en bout pour les messages échangés entre les clients et le serveur comme le fait WhatsApp. Pouyr cela, il faudrait chiffrer le message avant qu'il ne soit envoyé sur le réseau et le déchiffrer qu'à l'arriver.

# Chiffrement 

## 1)
Utiliser la fonction urandom pour générer des clés de chiffrement n'est pas recommandé car elle n'a pas été spécifiquement conçue pour la cryptographie et peut contenir des vulnérabilités inconnues qui pourraient être exploitées par des attaquants. Il est donc conseillé d'utiliser des bibliothèques cryptographiques dédiées telles que la bibliothèque Cryptographie de Python pour plus de sécurité.
## 2)

2. Pourquoi utiliser ses primitives cryptographiques peut être dangereux ?


En utilisant des primitives cryptographiques, il est important de les intégrer dans des protocoles de sécurité appropriés et de les implémenter correctement, car une mauvaise utilisation ou une implémentation incorrecte peut entraîner des vulnérabilités de sécurité. Il est donc conseillé d'utiliser des bibliothèques cryptographiques dédiées telles que la bibliothèque Cryptographie de Python pour plus de sécurité.

## 3 )
Le chiffrement en transit, tel que le chiffrement symétrique ou asymétrique, permet de protéger les données lorsqu'elles sont transférées entre l'utilisateur et le serveur. Cependant, une fois que les données atteignent le serveur, elles peuvent être stockées et utilisées à des fins malveillantes.




## 4)

La propriété d'intégrité manque ici. En effet, le message n'est pas signé, donc il est possible de modifier le message sans que le serveur ne s'en rende compte.

# Authenticated Symetric Encryption

## 1)

Fernet est une bibliothèque cryptographique dédiée à la cryptographie symétrique et à l'authentification. Elle est donc plus sûre à utiliser que les primitives cryptographiques de base telles que AES et HMAC. Cela garantit que les données sont protégées tout au long de leur trajet, qu'elles soient en transit ou stockées sur un serveur.
## 2)

L'attaque de rejeu (replay attack) est une attaque qui consiste à réutiliser un message déjà utilisé pour tromper les destinataires. Cela peut être fait en interceptant et en réutilisant un message qui a déjà été envoyé, ou en enregistrant et en réutilisant un message qui a déjà été reçu. Les attaques de rejeu peuvent être utilisées pour compromettre la confidentialité, l'intégrité ou l'authenticité des données.

## 3)


Une méthode simple pour s'en affranchir consiste à ajouter un numéro de séquence unique à chaque message. Le numéro de séquence est généralement inclus dans le message lui-même, mais il peut également être fourni séparément lors de l'appel à la fonction de déchiffrement. Le serveur peut vérifier que le numéro de séquence est unique et rejeter le message s'il a déjà été utilisé.

# TTL

## 1)

Oui, avec l'ajout du TTL, les messages ont une durée de vie limitée, ce qui renforce la sécurité en empêchant leur réutilisation à des moments ultérieurs. Les messages qui ont dépassé leur durée de vie ne seront pas pris en compte lors du décodage, ce qui empêche les attaquants de réutiliser des messages plus anciens pour essayer de tromper les destinataires.

## 2)

Le message est considéré comme expiré et ne doit pas être pris en compte lors du décodage. Cela est dû au fait que le TTL est un entier non signé, ce qui signifie qu'il ne peut pas être négatif. Si le TTL est dépassé, le message est considéré comme expiré et ne doit pas être pris en compte lors du décodage.
## 3)

Oui, le TTL est efficace pour se protéger de l'attaque du chapitre précédent car il empêche les attaquants de réutiliser des messages plus anciens pour essayer de tromper les destinataires. Une fois que le TTL est dépassé, le message est considéré comme expiré et ne doit pas être pris en compte lors du décodage.
## 4)
Cela peut poser problème si le temps de transmission varie, par exemple en cas de ralentissement ou d'interruption du réseau. Si le message prend plus de temps que prévu pour arriver à destination, il peut être considéré comme expiré et être ignoré, même s'il aurait dû être valide. De plus, si le temps de transmission est très court, il peut arriver que le message arrive à destination après l'expiration de son TTL, ce qui peut également causer des problèmes. Enfin, cette solution nécessite de synchroniser l'horloge des différents interlocuteurs pour être efficace.

# Regard critique


Le problème décrit dans le code peut être une vulnérabilité de sécurité majeure car cela permet à un attaquant de fournir des données malveillantes qui peuvent être acceptées et traitées par le serveur comme des données légitimes. Pour éviter cela, le serveur doit effectuer une vérification de l'authenticité du message avant de le déchiffrer. 
Le serveur n'est pas protégé contre les attaques de rejeu car il ne vérifie pas que le numéro de séquence est unique et rejette le message s'il a déjà été utilisé. Cela peut être fait en ajoutant un numéro de séquence unique à chaque message. Le numéro de séquence est généralement inclus dans le message lui-même, mais il peut également être fourni séparément lors de l'appel à la fonction de déchiffrement. Le serveur peut vérifier que le numéro de séquence est unique et rejeter le message s'il a déjà été utilisé.


