Bien sûr, voici une synthèse des erreurs que vous avez rencontrées et des solutions apportées :

### Erreur 1 : `pkg-config: not found`

#### Description
L'outil `pkg-config` n'a pas été trouvé sur votre système. `pkg-config` est utilisé pour gérer les bibliothèques et leurs dépendances.

#### Solution
Installez `pkg-config` en utilisant les commandes suivantes :

```sh
sudo apt update
sudo apt install pkg-config
```

### Erreur 2 : `cc: No such file or directory`

#### Description
Le compilateur `cc` (souvent un alias pour GCC ou Clang) n'a pas été trouvé sur votre système. Sans un compilateur C, il est impossible de compiler Redis.

#### Solution
Installez `build-essential` (qui inclut GCC et d'autres outils nécessaires) en utilisant les commandes suivantes :

```sh
sudo apt update
sudo apt install build-essential
```

### Erreur 3 : `fatal error: jemalloc/jemalloc.h: No such file or directory`

#### Description
Redis ne trouve pas les fichiers d'en-tête de `jemalloc`, une bibliothèque de gestion de mémoire utilisée par Redis pour améliorer les performances.

#### Solution
Installez `libjemalloc-dev` en utilisant les commandes suivantes :

```sh
sudo apt update
sudo apt install libjemalloc-dev
```

### Étapes complètes pour compiler et utiliser Redis

Pour compiler et utiliser Redis après avoir résolu les erreurs ci-dessus, suivez les étapes ci-dessous :

1. **Télécharger Redis**

    ```sh
    wget http://download.redis.io/releases/redis-6.0.10.tar.gz
    tar xzf redis-6.0.10.tar.gz
    cd redis-6.0.10
    ```

2. **Installer les dépendances nécessaires**

    ```sh
    sudo apt update
    sudo apt install build-essential pkg-config libjemalloc-dev
    ```

3. **Nettoyer les compilations précédentes et recompiler Redis**

    ```sh
    make distclean  # Nettoyer les compilations précédentes
    make
    ```

4. **Démarrer Redis en arrière-plan**

    ```sh
    src/redis-server &
    ```

5. **Vérifier que le serveur fonctionne**

    ```sh
    src/redis-cli ping
    ```

    Vous devriez voir la réponse `PONG`.

6. **Définir et obtenir des valeurs**

    ```sh
    src/redis-cli set Holberton School
    src/redis-cli get Holberton
    ```

    Vous devriez voir la sortie `"School"`.

7. **Arrêter le serveur Redis**

    ```sh
    ps aux | grep redis-server
    kill [PID_OF_Redis_Server]
    ```

8. **Copier le fichier `dump.rdb`**

    ```sh
    cp dump.rdb /path/to/alx-backend/0x03-queuing_system_in_js/
    ```

En suivant ces étapes, vous devriez être en mesure de compiler et d'utiliser Redis correctement. Si vous rencontrez d'autres problèmes, n'hésitez pas à le signaler.







// {
//   "dependencies": {
//     "redis": "^4.6.14"
//   }
// }
